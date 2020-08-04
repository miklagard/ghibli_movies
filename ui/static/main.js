// src/main.js
Vue.config.productionTip = false;

new Vue({
  el: '#app',
  components: { 'app-ghibli':  window.httpVueLoader('/static/components/App.vue') },
});