from django import forms


class AddArtForm(forms.Form):
    # required=True表示必填项
    # min_length表示最小长度
    title = forms.CharField(min_length=5, required=True,
                            error_messages={
                                'required': '文章标题是必填项',
                                'min_length': '文章标题不能少于5个字符'
                            })
    is_display = forms.CharField(required=True)

    desc = forms.CharField(min_length=2, required=True,
                           error_messages={
                               'required': '文章简短描述必填',
                               'min_length': '文章简短描述不能少于20字符'
                           })
    keyword = forms.CharField(min_length=2, required=True,
                           error_messages={
                               'required': '文章关键字描述必填',
                               'min_length': '文章关键字不能少于两个字符'
                           })
    content = forms.CharField(required=True,
                              error_messages={
                                  'required': '文章内容必填'
                              })
    icon = forms.ImageField(required=False)



class AddNotForm(forms.Form):
    title = forms.CharField(min_length=5, required=True,
                            error_messages={
                                'required': '文章标题是必填项',
                                'min_length': '文章标题不能少于5个字符'
                            })

    content = forms.CharField(required=True,
                              error_messages={
                                  'required': '文章内容必填'
                              })
    icon = forms.ImageField(required=False)
    is_display = forms.CharField(required=True)