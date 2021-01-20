public class Solution {

    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null){return l2;}
        if (l2 == null){return l1;}

//        printList(l1);
//        System.out.println();
//        printList(l2);
//        System.out.println();
//        System.out.println("*****");

        if(l1.val < l2.val){
            l1.next = mergeTwoLists(l1.next, l2);
            return l1;
        } else {
            printList(l2);
            System.out.println();
            l2.next = mergeTwoLists(l1, l2.next);
            return l2;
        }
    }

    static void printList(ListNode L1){
        int value = L1.val;

        while(true){
            System.out.print(value + " ");
            if (L1.next == null){
                break;
            }
            L1 = L1.next;
            value = L1.val;
        }
    }


    public static void main(String[] args) {
        ListNode head_1 = new ListNode(1);
        head_1.next = new ListNode(2);
        head_1.next.next = new ListNode(4);

        ListNode head_2 = new ListNode(1);
        head_2.next = new ListNode(3);
        head_2.next.next = new ListNode(4);

        //printList(L1);
        ListNode result = new Solution().mergeTwoLists(head_1, head_2);
        printList(result);
    }
}


