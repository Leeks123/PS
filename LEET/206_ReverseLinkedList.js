/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
 var reverseList = function(head) {
    const reverse = (prev,cur) => {
        if(cur == null) return cur;

        let next = cur.next;
        
        if(prev == null) {
            cur.next = null;
        } else {
            cur.next = prev;
        }
        
        if(next == null) {
            return cur;
        }
        
        return reverse(cur,next);
    }
    
    return reverse(null,head);
};
