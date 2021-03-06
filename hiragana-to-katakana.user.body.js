function hiraganaToKatakana(text) {
  return text.replace(/./gm, function(c) {
    return hiraganaToKatakanaMap[c] || c;
  });
}

function replaceText(node) {
  var ignoreNodes = ["script", "style"];
  for (var child = node.firstChild; child; child = child.nextSibling) {
    switch (child.nodeType) {
      case 1:
        if (ignoreNodes.indexOf(child.tagName.toLowerCase()) < 0) {
          replaceText(child);
        }
        break;
      case 3:
        var text = child.data;
        child.data = hiraganaToKatakana(text);
        break;
    }
  }
}

function doConversion() {
  replaceText(document.body);
}

doConversion();
