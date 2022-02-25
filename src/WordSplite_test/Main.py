# -*- coding: utf-8 -*-
import Get_day_data
import Get_keywords
import Get_keynews
import Delete_Repeat
import Get_hot_result
import Global_param
def main():
    # 1->32
    for i in range(1,Global_param.number_day):
        # 找到最后一次浏览的是第i天的新闻的用户行为，存放在test/train_lastday_set目录下。
        # 把数据集中，不同日期的新闻，分类存储到不同的文件中
        Get_day_data.TransforData(i)
        # 区分每一天的新闻，存放在test/train_date_set1目录下
        # 另一个数据集，和上一个有什么区别？
        Get_day_data.TransforDataset(i)
        # 调用jieba库，挑出每一天最火的分词，存放在test/key_words下
        Get_keywords.Get_keywords(i)
        # 进行新闻推荐
        Get_keynews.Get_keynews(i)
    Delete_Repeat.Delete_Repeat()
    Get_hot_result.get_hot_result(Global_param.hot_rate)

if __name__ == '__main__':
    main()