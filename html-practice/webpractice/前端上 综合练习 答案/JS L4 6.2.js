//使用两种方法在数组a=[1,2,3,4,5]的第一个元素前添加一个元素“0”，并将新的数组输出。
var a=[1,2,3,4,5];
//方法一
a.unshift(0);
document.write(a+"<br>");
//方法二
a.splice(0,0,0);
document.write(a);