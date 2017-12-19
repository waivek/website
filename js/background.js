var Dark = function()
{
    document.body.className = "dark";
};

var Light = function()
{
    document.body.className = "";
};

var LoadPreviewImages = function()
{
    div_tag = document.getElementsByClassName("imgcontainer")[0];
    var image_divs = 
        '<img class="preview" src="Light.png" onclick="Light()" alt="Click for a light theme" />' + 
        '<img class="preview" src="Dark.png"  onclick="Dark()"  alt="Click for a dark theme"  />' ;
    div_tag.innerHTML =  image_divs;
}
