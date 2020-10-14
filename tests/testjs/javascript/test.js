// document.write('<script type="text/javascript" charset="utf-8" src="iview/test1.js"></script>')
var el=document.querySelector('head')

var importjs=function(jspath){
    var newElement = document.createElement('script');
    newElement.setAttribute('type','text/javascript');
    newElement.setAttribute('src',jspath);
    el.appendChild(newElement)
    console.log('成功引入js')
}

var generateParentNode=function(el,classname){
    elem = document.createElement('div')
    elem.className=classname
    el.parentNode.replaceChild(elem,el)
    elem.appendChild(el)
}


importjs('javascript/test_1.js')
var testImportJs=function(){
    var a=test_1();
    return 'testImportJs-'+a+1
}



var creatVueApp=function(){ 
    const app3 = new Vue({
        el: '#app3',
        data() {
            return{
                msg:'引入js手动新建app3'
            }
        },
        methods:{
            testApp3Click(){
                this.msg='app3-测试vue点击'
            }
        }
    }).$mount('#app3')
}

document.addEventListener("DOMContentLoaded", function(event) {  
    const app4 = new Vue({
        el: '#app4',
        data() {
            return{
                msg:'引入js自动创建app4'
            }
        },
        methods:{
            testApp4Click(){
                this.msg='app4-测试vue点击'
            }
        }
    }).$mount('#app4')
})
