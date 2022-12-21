#include <stdio.h>

  int main ()
  {
     int  x=10;        // biến x lưu cái gì địa chỉ hay là giá trị của ô nhớ
     char y[25]="Hoa Xinh Gai<";    
     int *ptr;      // con trỏ ptr lưu cái gì địa chỉ hay là giá trị của ô nhớ
     ptr=&x;    //đúng hay sai giải thích tại đây
     ptr=x;     //đúng hay sai
     ptr=*x;    //đúng hay sai
     *ptr=x;    //đúng hay sai
     char * ptr2;
     ptr2=y;      // đúng hay sai
     ptr2=&y;     // đúng hay sai
     ptr2=*y;     // đúng hay sai
     *ptr2=*y;    // đúng hay sai

  
     printf(": %x\n", &x  );      // điền kết quả vào trong printf trước %x|| lệnh này in cái gì? 
     printf(": %s\n", y  );       // điền kết quả vào trong printf trước %x|| lệnh này in cái gì? giá trị?
     printf(": %x\n", &y  );      // điền kết quả vào trong printf trước %x|| lệnh này in cái gì? giá trị?

     printf(": %x\n", &ptr  );    // điền kết quả vào trong printf trước %x|| lệnh này in cái gì? 
     printf(": %x\n", ptr  );     // điền kết quả vào trong printf trước %x|| lệnh này in cái gì? 
     printf(": %d\n", *ptr  );    // điền kết quả vào trong printf trước %d|| lệnh này in cái gì? giá trị?
     printf(": %c\n", *ptr2  );   // điền kết quả vào trong printf trước %c|| lệnh này in cái gì? giá trị?
     printf(": %s\n", ptr2 );     // điền kết quả vào trong printf trước %s|| lệnh này in cái gì? giá trị?
     printf(": %x\n", &ptr2  );   // điền kết quả vào trong printf trước %d|| lệnh này in cái gì? 
     //                           // dùng con trỏ ptr2 in ra chữ 'X'  tương tự y[4]
     printf("\n===========================\n");
     printf("Chuc  hoc tot! \n");
  
     return 0;
  }