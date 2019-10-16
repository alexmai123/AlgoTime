public class LinkedList {
  Node head;

  static class Node {
    int data;
    Node next;

    Node(int d){
      data = d;
      next = null;
    }
  }

   void insert(int data){
    Node new_node = new Node(data);
    new_node.next = null;

    // list is empty
    Node curr = head;
    if (curr == null){
      head = new_node;
    }
    else{
      while (curr.next != null){
        curr = curr.next;
      }
      curr.next = new_node;
    }
  }

  public static LinkedList remove_end(LinkedList list){
    Node curr = list.head;
    if (curr == null){
      return list;
    }
    if (curr.next == null){
      list.head = null;
      return list;
    }
    while (curr.next.next != null){
      curr = curr.next;
    }
    curr.next = null;
    return list;
  }

  public static LinkedList remove(LinkedList list, int data){
    Node curr = list.head;

    if (curr == null){
      return list;
    }

    if (curr.data == data){
      list.head = curr.next;
      return list;
    }
    
    while (curr.next.next != null){
      if(curr.next.data == data){
        curr.next = curr.next.next;
        return list;
      }
      curr = curr.next;
    }
    return list;
  }

  public static void printList(LinkedList list){
    Node curr = list.head;

    System.out.print("Linkedlist: ");
    if (curr == null){
      System.out.print("is empty.");
      return;
    }
    while (curr.next != null){
      System.out.print(curr.data + "->");
      curr = curr.next;
    }
    System.out.print(curr.data);
  }

  public static void main(String[] args) {
    LinkedList list = new LinkedList();
    list.insert(1);
    list.insert(2);

    printList(list);
  }
}