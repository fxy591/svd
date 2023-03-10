import axios from 'axios';
import qs from 'qs';
import ViewUI from 'view-design';
let baseURL = '/admin/';
export default class Ajax {
    axios(method, url, params) {
        return new Promise((resolve, reject) => {
            if (typeof params !== 'object') params = {};
            let _option = {
                method,
                url,
                baseURL,
                timeout: 60000,
                params: null,
                data: null,
                headers: {'X-Requested-With': 'XMLHttpRequest'},
                ...params
            }
            if (_option.method === "get" && !_option.url.endsWith(".json")) {
              //解决ie下的请求缓存问题
              !_option.params ? (_option.params = { _t: new Date().valueOf() }) : Object.assign(
                    _option.params,
                    { _t: new Date().valueOf() }
                  );
            }
            if (_option.data!=null) {
                if (_option.headers!=null) {
                    if (_option.headers['Content-Type']!='multipart/form-data') {
                        _option.data = qs.stringify(_option.data,{allowDots: true});
                    }
                } else {
                    _option.data = qs.stringify(_option.data,{allowDots: true});
                }
            }
            axios.request(_option).then(res => {
                if(typeof(res.data) != 'object'){
                    console.error('exception:','URL未返回期望的json格式；Method：',_option.method,'URL:',_option.url)
                }else{
                    resolve(res.data)
                }
            }).catch(error => {
                reject(error);
                if (error.response) {
                    if(!!!_option.notips){
                        setTimeout(function () {
                            ViewUI.Message.error("服务异常，请稍后重试");
                        }, 500);
                    }
                } else if (error.code === 'ECONNABORTED' && error.message.indexOf('timeout') != -1) {
                    if(!!!_option.notips){
                        setTimeout(function () {
                            ViewUI.Message.error("请求超时，请稍后重试");
                        }, 500);
                    }
                } else {
                    if(!!!_option.notips){
                        setTimeout(function () {
                            ViewUI.Message.error("服务异常，请稍后重试");
                        }, 500);
                    }
                }
            });
        })
    }
}