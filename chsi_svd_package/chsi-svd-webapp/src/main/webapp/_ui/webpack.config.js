const path = require('path'),
    webpack = require('webpack'),
    ExtractTextPlugin = require('extract-text-webpack-plugin'); //抽取css
const Version = '1.0.0';
function resolve (dir) {
    return path.join(__dirname, dir);
}
module.exports = {
  entry: {
    app: ["babel-polyfill", "./src/main.js"]
  },
  externals: {
    vue: "Vue",
    "view-design": "iview"
  },
  output: {
    path: path.resolve(__dirname, '../assets/'),
    publicPath: '../',
    filename: "js/[name]-"+ Version +".js"
  },
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: "vue-loader",
        options: {
          loaders: {
            css: "vue-style-loader!css-loader",
            less: "vue-style-loader!css-loader!less-loader"
          },
          postLoaders: {
            html: "babel-loader"
          }
        }
      },
      {
        test: /\.css$/,
        use: ExtractTextPlugin.extract({
            use: [
                {
                    loader: "css-loader",
                    options: {
                        minimize: true
                    }
                },
                {
                    loader: "autoprefixer-loader"
                }
            ],
            fallback: "style-loader"
        })
      },
      {
        test: /\.js$/,
        loader: "babel-loader",
        exclude: /node_modules/
      },
      {
        test: /\.less/,
        use: ExtractTextPlugin.extract({
          use: [
            {
              loader: "css-loader",
              options: {
                minimize: true
              }
            },
            {
              loader: "autoprefixer-loader"
            },
            {
              loader: "less-loader?sourceMap",
              options: {
                strictMath: false,
                noIeCompat: true
              }
            }
          ],
          fallback: "style-loader"
        })
      },
      {
        test: /\.(gif|jpg|png|svg)\??.*$/,
        use: [
          {
            loader: "url-loader",
            options: {
              limit: 1024,
              name: "images/[name].[ext]"
            }
          }
        ]
      },
      {
        test: /\.(woff|eot|ttf)\??.*$/,
        use: [
          {
            loader: "url-loader",
            options: {
              limit: 1024, //设置大小会影响打包
              name: "font/[name].[ext]"
            }
          }
        ]
      }
    ]
  },
  plugins: [
    new ExtractTextPlugin({
      filename: "css/[name]-"+ Version +".css",
      publicPath: "../"
    }),
    new webpack.optimize.CommonsChunkPlugin({
      name: "vendors",
      filename: "js/vendors.js"
    }),
    new webpack.optimize.UglifyJsPlugin({
      compress: {
        warnings: false
      },
      sourceMap: false
    })
  ],
  resolve: {
    extensions: [".js", ".vue", ".less"],
    alias: {
      "@": resolve('src'),
      vue: "vue/dist/vue.js"
    }
  }
};