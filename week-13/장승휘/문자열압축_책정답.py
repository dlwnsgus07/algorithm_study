def solution(s):
    answer = len(s)

    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1
    
        for j in range(step, len(s), step):
        
            if prev == s[j:j + step]:
                count += 1
            
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step] # Prev 초기화
                count = 1
            
        # 남아 있는 문자열에 처리
        compressed += str(count) + prev if count >= 2 else prev
    
        answer = min(answer, len(compressed))

    return answer