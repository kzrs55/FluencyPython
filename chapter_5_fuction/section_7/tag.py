# -*- coding: utf-8 -*-

#从定位参数到仅限关键字参数

def tag(name, *content, cls=None, **attr):
    if cls is not None:
        attr['class'] = cls
    if attr:
        attr_str = ''.join(' %s="%s"' % (key, value) for key, value in attr.items())
    else:
        attr_str = ''
    if content:
        return '\n'.join("<%s%s>%s</%s>" % (name, attr_str, c, name) for c in content)
    else:
        return "<%s%s />" % (name,attr_str)


if __name__ == '__main__':
    print(tag('br'))
    print(tag('br', 'hello'))
    print(tag('p', 'hello', 'world'))
    print(tag('p', 'hello', id=33))
    print(tag('p', 'hello', 'world', cls='sidebar'))
    print(tag(content='testing', name="img"))
    my_tag = {'name':'img','title':'world','src':'code','cls':'class'}
    print(tag(**my_tag))
