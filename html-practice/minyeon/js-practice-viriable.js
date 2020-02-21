//在最后面添加文本信息
document.write("关于为什么要写这个页面");

//创建一个函数，在html调用
function openNewWindows() {
    alert("健康最重要，健康最重要，健康最重要");
}
//给id为div1的元素，删除一个p子元素在父元素的最后，如果是
var parent = document.getElementById("div1");
var child = document.getElementById("p1");
parent.removeChild(child);

//给id为div1的元素，创建一个p子元素在父元素的最后，如果是
var para = document.createElement("p");
var node = document.createTextNode("这是新段落。");
para.appendChild(node);
var element = document.getElementById("div1");
element.appendChild(para);

var pa = document.createElement("h1");
var node1 = document.createTextNode("健康最重要，健康最重要，健康最重要");
pa.appendChild(node1);
var element1 = document.getElementById("textList");
element1.appendChild(pa);

//创建一个video
//创建一个img
var amy1 = document.createElement("img");
amy1.src = "https://wx1.sinaimg.cn/mw690/7bddefb9ly1fhhhmio86sj204g07saac.jpg";
var amy2 = document.createElement("img");
amy2.src = "https://wx1.sinaimg.cn/mw690/7bddefb9ly1fhhhmio86sj204g07saac.jpg";
var mm = document.createElement("video");
mm.setAttribute("width", "800");
mm.setAttribute("height", "600");
mm.setAttribute("controls", "controls");
var nn = document.createElement("source");
nn.src = "https://static1.bcjiaoyu.com/0708scratch%E7%BB%98%E5%88%B6.mp4"
mm.appendChild(nn);
var element2 = document.getElementById("eunJung");
element2.appendChild(amy1);
element2.appendChild(mm);
element2.appendChild(amy2);