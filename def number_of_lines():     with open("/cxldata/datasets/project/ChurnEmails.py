def number_of_lines():
    with open("/cxldata/datasets/project/mbox-short.txt") as f:
        rf = f.read()
        c = 0
        for line in rf:
            if line == "\n":
                c+=1
        return c
res = number_of_lines()
print(res)

def count_number_of_lines():
    with open("/cxldata/datasets/project/mbox-short.txt") as f:
        c = 0
        for line in f:
            if line.startswith('Subject:'):
                c+=1
    return c
    
def average_spam_confidence():
    with open("/cxldata/datasets/project/mbox-short.txt") as f:
        c = 0
        sum = 0
        for line in f:
            if line.startswith("X-DSPAM-Confidence:"):
                c+=1
                sline = line.split()
                sum+=float(sline[1])
        return sum/c
res = average_spam_confidence()
print(res)

def find_email_sent_days():
    with open("/cxldata/datasets/project/mbox-short.txt") as f:
        cmon = 0
        ctue = 0
        cwed = 0
        cthu = 0
        cfri = 0
        csat = 0
        csun = 0
        dic = {}
        for line in f:
            if line.startswith("From"):
                sline = line.split()
                try:
                    day = sline[2]
                    if day == 'Mon':
                        cmon+=1
                    elif day == 'Tue':
                        ctue+=1
                    elif day == 'Wed':
                        cwed+=1
                    elif day == 'Thu':
                        cthu+=1
                    elif day == 'Fri':
                        cfri+=1
                    elif day == 'Sat':
                        csat+=1
                    else:
                        csun+=1
                except:
                    continue
        l = [cmon,ctue,cwed,cthu,cfri,csat,csun]
        if cmon != 0:
            dic['Mon'] = cmon
        if ctue != 0:
            dic['Tue'] = ctue
        if cwed != 0:
            dic['Wed'] = cwed
        if cthu != 0:
            dic['Thu'] = cthu
        if cfri != 0:
            dic['Fri'] = cfri
        if csat != 0:
            dic['Sat'] = csat
        if csun != 0:
            dic['Sun'] = csun
        return(dic)
    
print(find_email_sent_days())

def count_message_from_email():
    emaildict={}
    fhand=open('/cxldata/datasets/project/mbox-short.txt')
    for line in fhand:
        line = line.rstrip()
        if line.startswith('From:'):
            email = line.split(' ')[1]
            print(email)
            if email not in emaildict:
                emaildict[email] = 1
            else:
                emaildict[email]+=1
    return emaildict
    
def count_message_from_domain():
    domaindict = {}
    f = open("/cxldata/datasets/project/mbox-short.txt")
    for line in f:
        line = line.rstrip()
        if line.startswith('From:'):
            position = line.find('@')
            end_pos = line.find(' ',position)
            if end_pos == -1:
                domain = line[position+1:]
            else:
                domain = line[position+1: end_pos]
            if domain not in domaindict:
                domaindict[domain]=1
            else:
                domaindict[domain]+=1
    return domaindict
