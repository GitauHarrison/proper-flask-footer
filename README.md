# Add and Keep That Damn Footer at the Bottom

I have kept it minimal, only showing two pages:

**First page**:

Footer beneath the content, even when the content is taller than hte viewport.

![Taller Content with Footer](app/static/images/taller_content.png)

**Second page**:

Footer at the bottom of the page, leaving space between it and short content.

![Short Content with Footer](app/static/images/short_content.png)


## Using CSS

```css
body{
    min-height: 100vh;
    display: flex;
    flex-direction: column;
}
```

- We begin by making the page as long as the screen height.
- Set the `body`'s display to `flex` and flex its direction to `column`


```css
footer{
    margin-top: auto;
}
```
- To stick the footer to the bottom, set its top margin to `auto`.

### See it Yourself
Download project:

```python
$ git clone git@github.com:GitauHarrison/proper-flask-footer.git # you can use HTTP
```

Move into the project:

```python
$ cd proper-flask-footer
```
Activate your virtual environment:

```python
$ workon your-virtual-env
```

Install useful extensions or dependancies:

```python
$ pip3 install -r requirements.txt
```

Run application:

```python
$ flask run # check your localhost
```

Learn how to view your localhost project on another mobile device [here](https://github.com/GitauHarrison/notes/blob/master/localhost_testing.md).