import Vue from 'vue';
import ViewUI from 'view-design';
import '@/style/main.less';
import '@/style/style.less';
import api from '@/api/index';
import { data } from './js/data.js';
window.api = api;
Vue.use(ViewUI);
window.baseData = data;