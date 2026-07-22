class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        is_valid=True
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if len(stack)!=0:
                    if ((ch==']' and stack[-1]=='[') or (ch==')' and stack[-1]=='(') or (ch=='}' and stack [-1]=='{')):
                        stack.pop()
                    else:
                            is_valid=False
                else:
                    is_valid=False
                    break
        if len(stack)!=0:
            is_valid=False
        return is_valid


                