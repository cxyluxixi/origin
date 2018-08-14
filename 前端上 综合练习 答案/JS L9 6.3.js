//a = 12; b = 21;
// 给a和b排序并按字母顺序输出，
// 要保证从小到大排列
var a=12;
var b=21;
var t;
if(a>b)
{
    t=a;
    a=b;
    b=t;
}
document.write("a="+a+"<br>");
document.write("b="+b);