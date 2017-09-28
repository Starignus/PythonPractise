# Markdown Cheatsheet

Markdown is a text-to-HTML conversion tool for web writers. Markdown allows you to write using an easy-to-read, easy-to-write plain text format, then convert it to structurally valid XHTML (or HTML).
So our text can be converted into a formatted text with the use of ASCII-only punctuation marks and other non-letter symbols for tags.
For a complete reference to the Markdown Project you can refer to [its creator's website](https://daringfireball.net/projects/markdown/syntax).
**Note:** Github uses Github Flavoured Markdown, which is a variation of the original Markdown language. It adds some functionalities, that we have grouped under "Github Flavoured Markdown"

### Headers

```
# H1
## H2
### H3
#### H4
##### H5
###### H6
```
Alternatively, for H1 and H2, an underline-ish style:
```
Alt-H1
======

Alt-H2
------
```

# H1
## H2
### H3
#### H4
##### H5
###### H6

Alternatively, for H1 and H2, an underline-ish style:

Alt-H1
======

Alt-H2
------

### Emphasis

Emphasis, aka italics, with `*asterisks*` or `_underscores_`.

Strong emphasis, aka bold, with two `**asterisks**` or `__underscores__`.

Combined emphasis with `**asterisks and _underscores_**`.

Strikethrough uses two tildes. `~~Scratch this.~~`

Emphasis, aka italics, with *asterisks* or _underscores_.

Strong emphasis, aka bold, with **asterisks** or __underscores__.

Combined emphasis with **asterisks and _underscores_**.

Strikethrough uses two tildes. ~~Scratch this.~~

### Lists

```
(In this example, leading and trailing spaces are shown with with dots: ⋅)

1. First ordered list item
2. Another item
⋅⋅* Unordered sub-list.
1. Actual numbers don't matter, just that it's a number
⋅⋅1. Ordered sub-list
4. And another item.

⋅⋅⋅You can have properly indented paragraphs within list items. Notice the blank line above, and the leading spaces (at least one, but we'll use three here to also align the raw Markdown).

⋅⋅⋅To have a line break without a paragraph, you will need to use two trailing spaces.⋅⋅
⋅⋅⋅Note that this line is separate, but within the same paragraph.⋅⋅
⋅⋅⋅(This is contrary to the typical GFM line break behaviour, where trailing spaces are not required.)

* Unordered list can use asterisks
- Or minuses
+ Or pluses
```

1. First ordered list item
2. Another item
  * Unordered sub-list.
1. Actual numbers don't matter, just that it's a number
  1. Ordered sub-list
4. And another item.

   You can have properly indented paragraphs within list items. Notice the blank line above, and the leading spaces (at least one, but we'll use three here to also align the raw Markdown).

   To have a line break without a paragraph, you will need to use two trailing spaces.  
    Note that this line is separate, but within the same paragraph.
     (This is contrary to the typical GFM line break behaviour, where trailing spaces are not required.)

* Unordered list can use asterisks
- Or minuses
+ Or pluses

### Links

There are two ways to create links.
```
[I'm an inline-style link](https://www.google.com)

[I'm an inline-style link with title](https://www.google.com "Google's Homepage")

[I'm a reference-style link][Arbitrary case-insensitive reference text]

[I'm a relative reference to a repository file](../blob/master/LICENSE)

[You can use numbers for reference-style link definitions][1]

Or leave it empty and use the [link text itself].

URLs and URLs in angle brackets will automatically get turned into links.
http://www.example.com or <http://www.example.com> and sometimes
example.com (but not on Github, for example).
```

There are two ways to create links.

[I'm an inline-style link](https://www.google.com)

[I'm an inline-style link with title](https://www.google.com "Google's Homepage")

[I'm a reference-style link][Arbitrary case-insensitive reference text]

[I'm a relative reference to a repository file](../blob/master/LICENSE)

[You can use numbers for reference-style link definitions][1]

Or leave it empty and use the [link text itself].

URLs and URLs in angle brackets will automatically get turned into links.
http://www.example.com or <http://www.example.com> and sometimes
example.com (but not on Github, for example).

### Images

Here's Github mark (hover to see the title text):
```
![alt text](https://octodex.github.com/images/yaktocat.png "Logo Title Text 1")
```

![alt text](https://octodex.github.com/images/yaktocat.png "Logo Title Text 1")

### YouTube Videos

They can't be added directly but you can add an image with a link to the video like this using HTML tags:
```
<a href="http://www.youtube.com/watch?feature=player_embedded&v=YOUTUBE_VIDEO_ID_HERE
" target="_blank" ><img src="http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg"
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10"/></a>
```
<a href="http://www.youtube.com/watch?feature=player_embedded&v=YOUTUBE_VIDEO_ID_HERE
" target="blank" ><img src="http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg"
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10"/></a>  

Or, in pure Markdown, but losing the alt image sizing and border:  

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](http://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID_HERE)  

### Blockquotes

```
> Blockquotes are very handy in email to emulate reply text.
> This line is part of the same quote.

Quote break.

> This is a very long line that will still be quoted properly when it wraps. Oh boy let's keep writing to make sure this is long enough to actually wrap for everyone. Oh, you can *put* **Markdown** into a blockquote.
Blockquotes are very handy in email to emulate reply text. This line is part of the same quote.
Quote break.
```

> Blockquotes are very handy in email to emulate reply text.
> This line is part of the same quote.

Quote break.

> This is a very long line that will still be quoted properly when it wraps. Oh boy let's keep writing to make sure this is long enough to actually wrap for everyone. Oh, you can *put* **Markdown** into a blockquote.
Blockquotes are very handy in email to emulate reply text. This line is part of the same quote.
Quote break.

### Inline HTML

You can also use raw HTML in your Markdown, and it'll mostly work pretty well. It is especially useful for paragraph formatting.

```
<dl>
  <dt>Definition list</dt>
  <dd>Is something people use sometimes.</dd>

  <dt>Markdown in HTML</dt>
  <dd>Does *not* work **very** well. Use HTML <em>tags</em> for <b>formatting</b>.</dd>
</dl>
```
<dl>
  <dt>Definition list</dt>
  <dd>Is something people use sometimes.</dd>

  <dt>Markdown in HTML</dt>
  <dd>Does *not* work **very** well. Use HTML <em>tags</em> for <b>formatting</b>.</dd>
</dl>

### Horizontal Rule

Three or more...

\-\-\-

Hyphens

\*\*\*

Asterisks

\_\_\_

Underscores

Three or more...

---

Hyphens

***

Asterisks

___

Underscores

### Backlash to escape
Markdown allows you to use backslash escapes to generate literal characters which
would otherwise have special meaning in Markdown’s formaing syntax.
```
\*literal asterisks\*
```

\*literal asterisks\*

# Github Flavoured Markdown

The following features are not entirely part of the Markdown specs, but renderers (like Github) support these additional features. Some of them are especially useful when it come to version control.

### Code and Syntax Highlighting

Code blocks are part of the Markdown spec, but syntax highlighting is Github specific.

Inline \`code\` has \`back-ticks around\` it.
Inline `code` has `back-ticks around` it.

Blocks of code are either fenced by lines with three back-ticks \`\`\`, or are indented with four spaces. I recommend only using the fenced code blocks -- they're easier and only they support syntax highlighting.

\`\`\`  
   javascript  
   var s = "JavaScript syntax highlighting";  
   alert(s);  
\`\`\`  

\`\`\`  
   python  
   s = "Python syntax highlighting"  
   print s  
\`\`\`  

\`\`\`  
   No language indicated, so no syntax highlighting in Markdown Here (varies on Github).  
   But let's throw in a <b>tag</b>.  
\`\`\`  

```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```
```python
s = "Python syntax highlighting"
print s
```
```
No language indicated, so no syntax highlighting in Markdown Here (varies on Github).
But let's throw in a <b>tag</b>.
```

### Tables

Tables aren't part of the core Markdown spec, but they are part of Github Flavoured Markdown. They are an easy way of adding tables to your email -- a task that would otherwise require copy-pasting from another application.

Colons can be used to align columns.
<pre><span>

| Tables        | Are           | Cool  |  
| ------------- |:-------------:| -----:|  
| col 3 is      | right-aligned | $1600 |  
| col 2 is      | centered      |   $12 |  
| zebra stripes | are neat      |    $1 |  

</span></pre>

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

There must be at least 3 dashes separating each header cell.
The outer pipes (|) are optional, and you don't need to make the
raw Markdown line up prettily. You can also use inline Markdown.

<pre><span>
Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3
</pre></span>

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3

### Task Lists
```
- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
- [x] list syntax required (any unordered or ordered list supported)
- [x] this is a complete item
- [ ] this is an incomplete item
```
- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
- [x] list syntax required (any unordered or ordered list supported)
- [x] this is a complete item
- [ ] this is an incomplete item
If you include a task list in the first comment of an Issue, you will get a handy progress indicator in your issue list. It also works in Pull Requests!

### Issue references within a repository

Any number that refers to an Issue or Pull Request will be automatically converted into a link.
```
#1
mojombo#1
mojombo/github-flavored-markdown#1
```

### Username @mentions

Typing an @ symbol, followed by a username, will notify that person to come and view the comment. This is called an “@mention”, because you’re mentioning the individual. You can also @mention teams within an organization.


### Emoji

GitHub supports emoji! :sparkles: :camel: :boom:

To see a list of every image we support, check out the [Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet/).


<small>Based on Adam's Pritchard's [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) and Github's [Mastering Markdown](https://guides.github.com/features/mastering-markdown/)</small>
