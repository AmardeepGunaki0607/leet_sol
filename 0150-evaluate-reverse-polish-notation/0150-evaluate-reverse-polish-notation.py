class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]

        for ch in tokens:
            if ch =="+":
                a=st.pop()
                b=st.pop()
                st.append(a+b)
            elif ch =="-":
                a=st.pop()
                b=st.pop()
                st.append(b-a)

            elif ch =="*":
                a=st.pop()
                b=st.pop()
                st.append(a*b)

            elif ch =="/":
                a=st.pop()
                b=st.pop()
                st.append(int(b/a))
            else:
                st.append(int(ch))
        return st.pop()
        