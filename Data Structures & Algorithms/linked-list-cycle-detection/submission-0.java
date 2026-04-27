/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null || head.next == null) return false;
        ListNode hare = head, tort = head;
        while (hare.next != null && hare.next.next != null) {
            hare = hare.next.next;
            tort = tort.next;
            if (hare == tort) return true;
        }
        return false;
    }
}
