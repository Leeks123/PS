/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
 var inorderTraversal = function(root) {
    let ret = [];
    const traversal = (ret,node) => {
        // console.log(ret,node);
        if(node === null) return;
        
        traversal(ret,node.left);
        ret.push(node.val);
        traversal(ret,node.right);
    }
    traversal(ret,root);
    return ret;
};
