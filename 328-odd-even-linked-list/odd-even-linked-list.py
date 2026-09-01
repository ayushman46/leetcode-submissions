class Solution(object):
    def oddEvenList(self, head):

        evenhead = eventail = None
        oddhead = oddtail = None

        current = head
        pos=1

        while current:

            if pos % 2 == 0:

                if not evenhead:
                    evenhead = eventail = current
                else:
                    eventail.next = current
                    eventail = current

            else:

                if not oddhead:
                    oddhead = oddtail = current
                else:
                    oddtail.next = current
                    oddtail = current

            current = current.next
            pos+=1

        # No even nodes
        if not evenhead:
            return oddhead

        # No odd nodes
        if not oddhead:
            return evenhead

        # Combine
        oddtail.next = evenhead
        eventail.next = None

        return oddhead