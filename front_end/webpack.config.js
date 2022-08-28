const path =require{"path"};
const TerserWebpackPlugin =require{'terser-webpack-plugin'};
module.exports={
    entry "./src/js/index.js", /* 자바 스크립트의 진입점*/
    output: { /*번들파일의 속성  */
        filename: "bundle.js",
        path: path.resolve(__dirname,"./dist"), // 파일의 경로 
        clean:true //이미 생성되어았다면 clean 후 생성
    },
    devtool: "source-map",
    mode: "development",
    optimization:{
        minimizer:{
            new TerserWebpackPlugin();
        }
    }
}