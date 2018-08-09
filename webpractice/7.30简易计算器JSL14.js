/**
 * 
 * @authors Your Name (you@example.org)
 * @date    2018-07-31 11:47:44
 * @version $Id$
 */
 var addBtn=document.getElementById("add");
var subBtn=document.getElementById("sub");
var mulBtn=document.getElementById("mul");
var divBtn=document.getElementById("div");

var a_float;
var b_float;

function getInputNums(){
    var a=document.getElementById("num1").value;
    var b=document.getElementById("num2").value;
    a_float=parseFloat(a);
    b_float=parseFloat(b);
}

function sendResult(r){
    var show=document.getElementById("re");
    show.innerHTML=r;
}


function addtion(x,y){
    return x+y;
}
function substraction(x,y){
    return x-y;
}
function multiplication(x,y){
    return x*y;
}
function division(x,y){
    if(y==0){
        alert("0不能做除数");
        return null;
    }else{
        return x/y;
    }
}

addBtn.onclick=function() {
    getInputNums();
    var result=addtion(a_float,b_float);
    sendResult(result);
};
subBtn.onclick=function() {
    getInputNums();
    var result=substraction(a_float,b_float);
    sendResult(result);
};
mulBtn.onclick=function() {
    getInputNums();
    var result=multiplication(a_float,b_float);
    sendResult(result);
};
divBtn.onclick=function() {
    getInputNums();
    var result=division(a_float,b_float);
    sendResult(result);
};

