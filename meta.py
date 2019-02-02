# encoding: utf-8
import multiprocessing,os


def page_process(list_base_url, pi, save_dir, list_dir):
    page = str(pi + 1)
    print('processing page %s' % (page))
    list_url = list_base_url + '&page=' + page

    doc_urls = parse_links(list_url)

    for i, doc_url in enumerate(doc_urls):
        name_arr = doc_url.split('/')
        doc_path = os.path.join(save_dir, name_arr[-3], name_arr[-2])
        if not os.path.isdir(doc_path):
            os.makedirs(doc_path)

        # save list
        list_path = os.path.join(list_dir, name_arr[-3] + '_' + name_arr[-2] + '.txt')
        with open(list_path, 'a+') as f_list:
            f_list.write(doc_url + '\n')

        doc_name = name_arr[-1]
        doc_dir = os.path.join(doc_path, doc_name)
        if os.path.isfile(doc_dir):
            continue

        print('download doc %d: %s' % (i, doc_url))
        html = download(doc_url)
        if html is None:
            continue

        html_objs = BeautifulSoup(html, 'html.parser')
        with open(doc_dir, 'w') as f_html:
            f_html.write(str(html_objs))

def download_main(q=keyword, newstypeid='54', save_dir='data/html/', list_dir='data/url_list/'):
    list_base_url = 'http://wx.ajxxgk.jcy.gov.cn/index.php?m=search&c=index&a=init&typeid=&q=' + quote(
        q) + '&siteid=1&newstypeid=' + newstypeid + '&time=all'

    n_pages = get_page_number(list_base_url)
    print('total pages: %d' % (n_pages))  # 13304

    n_proc = 10
    pool = multiprocessing.Pool(processes=n_proc)

    for pi in range(n_pages - 1, 0, -1):
        if pi >= 13061: continue

        pool.apply_async(page_process, (list_base_url, pi, save_dir, list_dir))
        time.sleep(0.99)