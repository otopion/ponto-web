const path = require("path");
const LodashModuleReplacementPlugin = require("lodash-webpack-plugin");
const isProduction = process.env.NODE_ENV === "production";

module.exports = {
  publicPath: isProduction ? "/static/core/" : "/",
  indexPath: "../../templates/core/index.html",
  /**
   * Adicionar os caminhos do vtk js pois o mesmo necessita de ser
   * transpilado pelo babel
   *
   * ref: https://cli.vuejs.org/config/#transpiledependencies
   */
  transpileDependencies: [],
  css: {
    sourceMap: !isProduction,
    loaderOptions: {
    }
  },
  devServer: {
    serveIndex: false,
    proxy: {
      "/api": {
        target: "http://localhost:8001",
        changeOrigin: true
      },
      "/admin": {
        target: "http://localhost:8001",
        changeOrigin: true
      }
    }
  },
  configureWebpack(config) {
    if (!isProduction) {
      config.devtool = "source-map";
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
