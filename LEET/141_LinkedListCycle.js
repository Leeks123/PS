/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
 var hasCycle = function(head) {
    let visited = [];
    let cur = head;
    
    while(true) {
        if(cur == null) return false;
        if(visited.includes(cur)) {
            return true;
        } else {
            visited.push(cur);
            cur = cur.next;
        }
    }
};