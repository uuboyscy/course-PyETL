import requests
import json
import pprint

# https://www.newmobilelife.com/
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}
url = 'https://www.newmobilelife.com/wp-admin/admin-ajax.php?td_theme_name=Newspaper&v=10.3.5'

ss = requests.session()
#
# for page in range(0,10):
#     d = {'action': 'td_ajax_block','td_block_id': 'tdi_32_d14', 'td_column_number': '3', 'td_current_page': str(page+1), 'block_type': 'td_block_3'}
#
#     soup = BeautifulSoup(json.loads(ss.post(url, headers=headers, data=d).text)['td_data'], 'html.parser')
#     for t in soup.select('div[class="td-module-thumb"] a'):
#         print(t['title'])
#         print(t['href'])
#         print()

page = 0
tt = {
    "custom_title": "新產品",
    "category_id": "1409",
    "limit": "6",
    "ajax_pagination": "load_more",
    "separator": "",
    "custom_url": "",
    "block_template_id": "",
    "m1_tl": "",
    "post_ids": "",
    "category_ids": "",
    "tag_slug": "",
    "autors_id": "",
    "installed_post_types": "",
    "sort": "",
    "offset": "",
    "show_modified_date": "",
    "el_class": "",
    "td_ajax_filter_type": "",
    "td_ajax_filter_ids": "",
    "td_filter_default_txt": "All",
    "td_ajax_preloading": "",
    "f_header_font_header": "",
    "f_header_font_title": "Block header",
    "f_header_font_settings": "",
    "f_header_font_family": "",
    "f_header_font_size": "",
    "f_header_font_line_height": "",
    "f_header_font_style": "",
    "f_header_font_weight": "",
    "f_header_font_transform": "",
    "f_header_font_spacing": "",
    "f_header_": "",
    "f_ajax_font_title": "Ajax categories",
    "f_ajax_font_settings": "",
    "f_ajax_font_family": "",
    "f_ajax_font_size": "",
    "f_ajax_font_line_height": "",
    "f_ajax_font_style": "",
    "f_ajax_font_weight": "",
    "f_ajax_font_transform": "",
    "f_ajax_font_spacing": "",
    "f_ajax_": "",
    "f_more_font_title": "Load more button",
    "f_more_font_settings": "",
    "f_more_font_family": "",
    "f_more_font_size": "",
    "f_more_font_line_height": "",
    "f_more_font_style": "",
    "f_more_font_weight": "",
    "f_more_font_transform": "",
    "f_more_font_spacing": "",
    "f_more_": "",
    "m1f_title_font_header": "",
    "m1f_title_font_title": "Article title",
    "m1f_title_font_settings": "",
    "m1f_title_font_family": "",
    "m1f_title_font_size": "",
    "m1f_title_font_line_height": "",
    "m1f_title_font_style": "",
    "m1f_title_font_weight": "",
    "m1f_title_font_transform": "",
    "m1f_title_font_spacing": "",
    "m1f_title_": "",
    "m1f_cat_font_title": "Article category tag",
    "m1f_cat_font_settings": "",
    "m1f_cat_font_family": "",
    "m1f_cat_font_size": "",
    "m1f_cat_font_line_height": "",
    "m1f_cat_font_style": "",
    "m1f_cat_font_weight": "",
    "m1f_cat_font_transform": "",
    "m1f_cat_font_spacing": "",
    "m1f_cat_": "",
    "m1f_meta_font_title": "Article meta info",
    "m1f_meta_font_settings": "",
    "m1f_meta_font_family": "",
    "m1f_meta_font_size": "",
    "m1f_meta_font_line_height": "",
    "m1f_meta_font_style": "",
    "m1f_meta_font_weight": "",
    "m1f_meta_font_transform": "",
    "m1f_meta_font_spacing": "",
    "m1f_meta_": "",
    "ajax_pagination_infinite_stop": "",
    "css": "",
    "tdc_css": "",
    "td_column_number": 3,
    "header_color": "",
    "color_preset": "",
    "border_top": "",
    "class": "tdi_32_d14",
    "tdc_css_class": "tdi_32_d14",
    "tdc_css_class_style": "tdi_32_d14_rand_style",
}
d = {
    'action': 'td_ajax_block',
    'td_block_id': 'tdi_32_d14',
    'td_column_number': '3',
    'td_current_page': str(page + 1),
    'block_type': 'td_block_3',
    'td_magic_token': '5379568fbf',
}
res = ss.post(url, headers=headers, data=d)
pprint.pprint(json.loads(res.text))
