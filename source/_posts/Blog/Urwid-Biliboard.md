---
title: "Urwid B站 up主信息实时显示的TUI应用 updating..."
description: "Urwid B站 up主信息实时显示的TUI应用 updating..."
url: suxiv3
date: 2020/06/26
toc: true
excerpt: "Urwid B站 up主信息实时显示的TUI应用(已放棄)"
tags: [Python, Urwid]
category: [Python, TUI, Urwid]
cover: 'https://s1.ax1x.com/2020/06/26/NskXIx.png'
thumbnail: 'https://s1.ax1x.com/2020/06/26/NskXIx.png'
priority: 10000
---

## Urwid B站 up主信息实时显示的TUI应用 updating...



```python
import urwid, time, sys, ast, requests, json
from urllib.request import urlopen


class BiliSpider:
    def __init__(self):
        self.online_api = "https://api.bilibili.com/x/web-interface/online"  # 在线人数
        self.video_api = "https://api.bilibili.com/x/web-interface/archive/stat?&aid=%s"    # 视频信息
        self.newlist_api = "https://api.bilibili.com/x/web-interface/newlist?&rid=%s&pn=%s&ps=%s"     # 最新视频信息
        self.region_api = "https://api.bilibili.com/x/web-interface/dynamic/region?&rid=%s&pn=%s&ps=%s"  # 最新动态信息
        self.member_api = "http://space.bilibili.com/ajax/member/GetInfo"  # 用户信息
        self.stat_api = "https://api.bilibili.com/x/relation/stat?vmid=%s"  # 用户关注数和粉丝总数
        self.upstat_api = "https://api.bilibili.com/x/space/upstat?mid=%s"     # 用户总播放量和总阅读量
        self.follower_api = "https://api.bilibili.com/x/relation/followings?vmid=%s&pn=%s&ps=%s"    # 用户关注信息
        self.fans_api = "https://api.bilibili.com/x/relation/followers?vmid=%s&pn=%s&ps=%s"    # 用户粉丝信息
    #
    def get_api(api_url):
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Host": "api.bilibili.com",
            "Referer": "https://www.bilibili.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
        }
        res = requests.get(api_url, headers=headers)
        res_dict = res.json()
        return res_dict
    #
    def get_online(self):
        """
        获取在线信息
        all_count: 最新投稿
        web_online: 在线人数
        :return:
        """
        online_dic = BiliSpider.get_api(self.online_api)
        return online_dic
    #
    def get_video_info(self, aid):
        """
        获取视频信息
        :param aid: 视频id
        :return:
        """
        res = BiliSpider.get_api(self.video_api %aid)
        # print(res)
        return res
    #
    def get_newlist_info(self, rid, pn, ps):
        """
        获取最新视频信息
        :param rid: 二级标题的id (详见tid_info.txt)
        :param pn:  页数
        :param ps:  每页条目数 1-50
        :return:
        """
        res = BiliSpider.get_api(self.newlist_api %(rid, pn, ps))
        return res
    #
    def get_region_info(self, rid, pn, ps):
        """
        获取最新视频信息
        :param rid: 二级标题的id (详见tid_info.txt)
        :param pn:  页数
        :param ps:  每页条目数 1-50
        :return:
        """
        res = BiliSpider.get_api(self.region_api %(rid, pn, ps))
        return res
    #
    def get_member_info(self, mid):
        """
        获取用户信息
        :param mid:用户id
        :return:
        """
        post_data = {
            "crsf": "",
            "mid": mid,
        }
        header = {
            "Host": "space.bilibili.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Referer": "https://www.bilibili.com/",
        }
        res = requests.post(self.member_api, data=post_data, headers=header)
        member_dic = json.dumps(res.json(), ensure_ascii=False)
        return member_dic
    #
    def get_stat_info(self, vmid):
        """
        获取某用户的关注数和粉丝总数
        :param vmid: 用户id
        :return:
        """
        res = BiliSpider.get_api(self.stat_api % vmid)
        return res
    #
    def get_upstat_info(self, mid):
        """
        获取某用户的总播放量和总阅读量
        :param mid: 用户id
        :return:
        """
        res = BiliSpider.get_api(self.upstat_api % mid)
        return res
    #
    def get_follower_info(self, vmid, pn, ps):
        """
        获取某用户关注者信息
        :param vmid:用户id
        :param pn:  页数 最多5页
        :param ps:  每页条目数 1-50
        :return:
        """
        res = BiliSpider.get_api(self.follower_api %(vmid, pn, ps))
        return res
    #
    def get_fans_info(self, vmid, pn, ps):
        """
        获取某用户粉丝信息
        :param vmid:用户id
        :param pn:  页数 最多5页
        :param ps:  每页条目数 1-50
        :return:
        """
        res = BiliSpider.get_api(self.fans_api %(vmid, pn, ps))
        return res

bili = BiliSpider()

def Bili_v(Title,ID):
    ID = str(ID)
    url = "http://api.bilibili.com/archive_stat/stat?aid=" + ID
    html = urlopen(url).read().decode('utf-8')
    d = ast.literal_eval(html)
    Cont = d['data']
    View    = str(Cont['view'])
    Like    = str(Cont['like'])
    Reply   = str(Cont['reply'])
    Coin    = str(Cont['coin'])
    Result = "\n".join([Title,View, Like, Reply, Coin])
    return Result

def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()

palette = [
    ('banner', 'black', 'light gray'),
    ('streak', 'black', 'dark red'),
    ('bg', 'black', 'dark blue'),]
A = 'Test'

class Refresh:
    def keypress(self, key):
        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()
    def setup_view(self):
        #Self infor
        mid = 393056819
        AA = bili.get_member_info(mid)
        粉丝 = urwid.Text(str(bili.get_stat_info(mid)['data']['follower']))
        #Veido Infor
        Title = urwid.Text("\n".join(["","观看量:","点赞:","回复:","硬币:" ]))
        Bv1 = urwid.Text(Bili_v("Python色差",86328254))
        Bv2 = urwid.Text(Bili_v("汪汪洗澡",89026731))
        Bv3 = urwid.Text(Bili_v("大生态缸",61040198))
        Bv4 = urwid.Text(Bili_v("OneNote记",44637823))
        Bv5 = urwid.Text(Bili_v("OneNote2",45117221))
        self.Vedio_inf = urwid.Columns([Title,Bv1,Bv2,Bv3,Bv4,Bv5])

        Fan = urwid.AttrWrap( 粉丝,'header')
        self.Vedio_inf = urwid.AttrWrap(self.Vedio_inf, 'body')

        self.view = urwid.Padding(self.Vedio_inf, 'left')
        #self.view = urwid.ListBox(urwid.SimpleListWalker([self.Vedio_inf,urwid.Divider(),self.Vedio_inf]))
        self.view = urwid.AttrMap(self.view, 'body')
        self.view = urwid.Filler(self.Vedio_inf, 'middle')
        #self.view = urwid.Frame(header=粉丝, body=self.Vedio_inf)


    def main(self):
        self.setup_view()
        loop = urwid.MainLoop(
            self.view, palette=[('body', 'dark cyan', '')],
            unhandled_input=self.keypress)
        loop.set_alarm_in(1, self.refresh)
        loop.run()

    def refresh(self, loop=None, data=None):
        self.setup_view()
        loop.widget = self.view
        loop.set_alarm_in(5, self.refresh)


if __name__ == '__main__':
    refresh = Refresh()
    sys.exit(refresh.main())

```

![NskXIx.png](https://s1.ax1x.com/2020/06/26/NskXIx.png)
= = <br />实时刷新有了 = =不过排版一加东西就错误= = <br />下次再来
