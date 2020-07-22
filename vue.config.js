const path = require("path");
const LodashModuleReplacementPlugin = require("lodash-webpack-plugin");
const isProduction = process.env.NODE_ENV === "production";


let url = "";
if(isProduction)
 url = "http://backend-ponto.herokuapp.com";
else
  url = "http://127.0.0.1:8001";

module.exports = {
  transpileDependencies: [],
  configureWebpack: {
    performance: {
      hints: "warning", // enum
      maxAssetSize: 9048576, // int (in bytes),
      maxEntrypointSize: 9048576, // int (in bytes)
    }
  },
  css: {
    sourceMap: !isProduction,
    loaderOptions: {
    }
  },
  devServer: {
    serveIndex: false,
    disableHostCheck: true,
    compress: true,
    proxy: {
      "/api": {
        target: url,
        changeOrigin: true,
        secure: false
      },
      "/admin": {
        target: url,
        changeOrigin: true,
        secure: false
      }
    }
  },
  chainWebpack(config) {
    if (isProduction) {
      config.plugin("lodash").use(LodashModuleReplacementPlugin);
    } else {
      config.resolve.alias.set("@tests", path.join(__dirname, "tests", "unit"));
    }

    config.plugin("html").tap(args => [
      {
        ...args[0],
        minify: false
      }
    ]);
  }
};
