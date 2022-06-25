// pushbutton_irq_handler.c
#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/init.h>
#include <linux/interrupt.h>
#include <asm/io.h>
MODULE_LICENSE("GPL");
MODULE_AUTHOR("Altera University Program, modified by skyun");
MODULE_DESCRIPTION("DE1SoC Pushbutton Interrupt Handler");
#define LW_BRIDGE_BASE 0xFF200000
#define LW_BRIDGE_SPAN 0x00200000
#define LEDR_BASE 0x00
#define KEY_BASE 0x50
#define INTMASK 0x8
#define EDGE 0xC
#define IRQ_KEYS 73
void *lwbridgebase;
void *ledr_addr, *key_addr;
irq_handler_t irq_handler(int irq, void *dev_id, struct pt_regs *regs) //interrup handler type으로 irq_handler 선언 
{
int value;
value = ioread32(ledr_addr);
iowrite32(value + 1, ledr_addr);
iowrite32(0xf, key_addr + EDGE);
return (irq_handler_t) IRQ_HANDLED;
}
static int __init intitialize_pushbutton_handler(void) // pushbutton handler 초기화 함수 
{

lwbridgebase = ioremap_nocache(LW_BRIDGE_BASE, LW_BRIDGE_SPAN);  // lwbeidgebase = 0xFF200000~ 0xFF400000 까지의 가상주소 매핑
ledr_addr = lwbridgebase + LEDR_BASE; // LED 가상주소 매핑 0xFF200000 + 0x00 -> 0xFF200000
key_addr = lwbridgebase + KEY_BASE; // key(입력값 버튼클릭) 가상주소 매핑 0xFF20000+0x50-> 0xFF20050
// Set LEDs to 0x200 (the leftmost LED will turn on)
iowrite32(0x200, ledr_addr); // LED 에 10 0000 0000 을 write -> 10개 버튼중 가장 왼쪽(최상위 비트) LED 활성화 
// Clear the PIO edgecapture register (clear any pending interrupt)
iowrite32(0xf, key_addr + INTMASK); // 0xFF20058 : interruptmask register를 1111 로 활성화 
// Enable IRQ generation for the 4 buttons
iowrite32(0xf, key_addr + EDGE);  //0xFF2005C 의 edgecapture register 를 1111로 활성화 
// Register the interrupt handler.

return request_irq(IRQ_KEYS, (irq_handler_t)irq_handler, // 초기화 함수 내에 return request_irq() 선언
IRQF_SHARED, "pushbutton_irq_handler",
(void *)(irq_handler)); 
}

static void __exit cleanup_pushbutton_handler(void)
{

iowrite32(0x0, ledr_addr); //종료시 LED 0000  -> LED off
free_irq(IRQ_KEYS, (void*) irq_handler); //종료후 irq_handler 가 사용한 자원 (메모리 ? cpu?) 반납
}


module_init(intitialize_pushbutton_handler);// 커널에 pushbutton 초기화 함수 등록 (매크로)
module_exit(cleanup_pushbutton_handler);// 커널에 exit 함수 등록 (매크로))