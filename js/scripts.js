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
	var light_data_uri = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA8AAAALQAgMAAAAiGfEnAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAJUExURf///wAAAH9/f0nhj6QAAAAZdEVYdFNvZnR3YXJlAE1pY3Jvc29mdCBPZmZpY2V/7TVxAAAACXBIWXMAAA7EAAAOxAGVKw4bAAABBklEQVR42u3dUQ0AIAxDwSGSf/yrwMNCsjTcOXgG2ioAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgDxrjzqCBQsWLFjwz8EAAAAAAAAAAAAAAAAAAAAAAAAAAAAA4QxqCxYsWLBgwW4PAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJoMagsWLFiwYMFuDwAAAAAAAAAAAAAAAAAAAAAAAAAAAIBX7EsLFixYsGDBXgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAmgxqCxYsWLBgwW4PAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJoMagsWLFiwYMFuDwAAAAAAAAAAAAAAAAAAAAAAAAAAAACAZBdqY+q6tWqFhwAAAABJRU5ErkJggg==";
	var dark_data_uri = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA8AAAALQAQMAAABluYv3AAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAGUExURURERObm5mSJf2MAAAAZdEVYdFNvZnR3YXJlAE1pY3Jvc29mdCBPZmZpY2V/7TVxAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAAoUlEQVR42u3bsQkAIAxFwWzi/htaCDqAZQIGuVsgvP4nAgAAAAAAAAAAAAAA+hg7Zb46vBQrVgwAAAAAAAAAAAAA0JUpu2LF3hUAAAAAAAAAAAAAAIqZsitW7F0BAAAAAAAAAAAAAPiVRblixb4GAAAAAAAAAAAAAACKmbIrVuxdAQAAAAAAAAAAAACgmCm7YsXeFQAAAAAAAAAAAAAA4HYAwavJtg/9eHYAAAAASUVORK5CYII=";
    div_tag = document.getElementsByClassName("imgcontainer")[0];
    var image_divs = 
        '<img class="preview" src="' + light_data_uri + '" onclick="Light()" alt="Click for a light theme" />' + 
        '<img class="preview" src="' + dark_data_uri + '"  onclick="Dark()"  alt="Click for a dark theme"  />' ;
    div_tag.innerHTML =  image_divs;
}
