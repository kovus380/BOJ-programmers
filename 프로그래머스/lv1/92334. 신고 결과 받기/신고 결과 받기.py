from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    mail_cnt = []
    report_dict = defaultdict(set)
    for rep in report:
        a, b = rep.split()
        report_dict[b].add(a)
    for key, value in report_dict.items():
        if len(value) >= k:
            mail_cnt += list(value)
    answer = [mail_cnt.count(i) for i in id_list]
    return answer