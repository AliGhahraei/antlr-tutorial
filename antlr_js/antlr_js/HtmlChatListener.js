let ChatListener = require('./ChatListener').ChatListener;

const HtmlChatListener = function(res) {
    this.Res = res;    
    ChatListener.call(this); // inherit default listener
    return this;
};

// inherit default listener
HtmlChatListener.prototype = Object.create(ChatListener.prototype);
HtmlChatListener.prototype.constructor = HtmlChatListener;

HtmlChatListener.prototype.enterName = function(_) {
    this.Res.write("<strong>");    
};

HtmlChatListener.prototype.exitName = function(ctx) {      
    this.Res.write(ctx.WORD().getText());
    this.Res.write("</strong> ");
}; 

HtmlChatListener.prototype.exitEmoticon = function(ctx) {      
    let emoticon = ctx.getText();
    
    if(emoticon === ':-)' || emoticon === ':)')
    {
        this.Res.write("🙂");        
    }
    
    if(emoticon === ':-(' || emoticon === ':(')
    {
        this.Res.write("🙁");            
    }
}; 

HtmlChatListener.prototype.enterCommand = function(ctx) {          
    if(ctx.SAYS() != null)
        this.Res.write(ctx.SAYS().getText() + ':' + '<p>');

    if(ctx.SHOUTS() != null)
        this.Res.write(ctx.SHOUTS().getText() + ':' + '<p style="text-transform: uppercase">');
};

HtmlChatListener.prototype.exitLine = function(_) {
    this.Res.write("</p>");
};

HtmlChatListener.prototype.enterColor = function(ctx) {
    let color = ctx.WORD().getText();
    this.Res.write('<span style="color: ' + color + '">');
};

HtmlChatListener.prototype.exitColor = function(ctx) {
    this.Res.write("</span>");
};

HtmlChatListener.prototype.exitMessage = function(ctx) {
    this.Res.write(ctx.getText());
};

exports.HtmlChatListener = HtmlChatListener;
