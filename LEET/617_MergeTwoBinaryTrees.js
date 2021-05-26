/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {TreeNode}
 */
 var mergeTrees = function(root1, root2) {
    if(root1 == null) return root2;
    if(root2 == null) return root1;
    
    root1.val += root2.val;
    
    if(root1.left && root2.left) {
        mergeTrees(root1.left,root2.left);
    }
    if(root1.right && root2.right) {
        mergeTrees(root1.right,root2.right);
    }
    if(root1.left == null && root2.left !== null) {
        root1.left = root2.left;
    }
    if(root1.right == null && root2.right !== null) {
        root1.right = root2.right;
    }
    
    return root1;
};

