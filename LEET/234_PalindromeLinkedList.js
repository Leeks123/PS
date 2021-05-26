/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
 var isPalindrome = function(head) {
    const listLength = (start) => {
        if(start.next == null) return 1;
        else {
            return 1+listLength(start.next);
        }
    }
    const len = listLength(head);
    const list = [];
    const getListVal = function(node) {
        if(node == null) {
            return;
        } else {
            list.push(node.val);
            getListVal(node.next);
        }
    }
    getListVal(head);
    
    for(let i=0;i<Math.floor(list.length/2);i++){
        if(list[i] !== list[list.length-i-1]) return false;
    }
    return true;
};
