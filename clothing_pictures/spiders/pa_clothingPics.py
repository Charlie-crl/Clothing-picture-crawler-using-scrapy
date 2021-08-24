
import scrapy
import re
from clothing_pictures.items import ClothingPicturesItem

# 爬穿针引线官网作品之设计稿645页图片
class PaClothingpicsSpider(scrapy.Spider):
    name = 'pa_clothingPics'
    allowed_domains = ['www.eeff.net/']
    start_urls = ['http://www.eeff.net/forum.php?mod=forumdisplay&fid=1&filter=typeid&typeid=1']
    # 计数器：页数
    offset = 1
    def parse(self, response):

        if self.offset > 645:
            return
        else:

            cover_listData = re.findall(r'<a href="(.*?)" class="thread-thumb-wrap" title="(.*?)" target="_blank">',response.text)
            a = 'http://www.eeff.net'
            for tuple_data in cover_listData:
                yield scrapy.Request(url=a + tuple_data[0], callback=self.second_parse,dont_filter=True)
            self.offset = self.offset + 1
            yield scrapy.Request(url='https://www.eeff.net/forum.php?mod=forumdisplay&fid=1&typeid=1&typeid=1&filter=typeid&page=' + str(self.offset) , callback=self.parse, dont_filter=True)

    def second_parse(self,response):
        item = ClothingPicturesItem()
        img_list = response.xpath('//td[@class="t_f"]/img/@file').extract()
        item['picture_urls'] = img_list
        yield item


