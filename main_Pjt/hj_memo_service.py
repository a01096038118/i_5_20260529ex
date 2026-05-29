class MemoService:
     
    def __init__(self, memoList):
        self.memoList = memoList

    def getTime(self, memo):
        return memo['작성시간']

    def readLatest(self):
        self.memoList.sort(key=self.getTime, reverse=True)
        
        for memo in self.memoList:
            for key, value in memo.items():
                print(f'{key}: {value}')
            print('-' * 40)
            
    def readOldest(self):
        self.memoList.sort(key=self.getTime)
        
        for memo in self.memoList:
            for key, value in memo.items():
                print(f'{key}: {value}')
            print('-' * 40)    

    def readMonth(self):
        memoReadMonth = input('조회 월을 입력: [숫자 두자리로 입력하세요. ex) 5월 -> 05] ')
        for memo in self.memoList:
            monthMemo = memo['작성시간'].split('-')[1]
            if memoReadMonth == monthMemo:
                print(memo)

    def showMemoList(self):
        for idx, memo in enumerate(self.memoList):
            print(f'{idx}. {memo}')

    def modifyMemo(self, modifyNum, newMemo):
        self.memoList[modifyNum]['메모내용'] = newMemo

    def deleteMemo(self, deleteNum):
        return self.memoList.pop(deleteNum)
        