#include<stdio.h>

int box[3];
int box_flag[3]={0};

int num_flag[10]={0};
int total = 0;

/*
三个不同盒子里，放0到9数的问题
深度优先搜索 depth first search
*/
void put_to_box(int box_id)
{
       //判断边界条件
       if (box_id==3)
       {
            printf("%d %d %d\n",box[0],box[1],box[2]);
            box_id=0;
            total++;
            return ;
       }

        //遍历会一种情况
       for (int i=0;i<10;i++)
       {
            //10x9x8=720 10个球不能重复的情况
//           if ( num_flag[i]==0)// 如果i球没有放过
//           {
//            num_flag[i]=1;
//            box[box_id]=i;
//            put_to_box(box_id+1);
//            num_flag[i]=0;
//           }

        //第一个球不能为0的情况，且三个数不能重复
           if(i==0 && box_id==0)
           {
               continue;
           }
           if ( num_flag[i]==0)// 如果i球没有放过
           {
            num_flag[i]=1;
            box[box_id]=i;
            put_to_box(box_id+1);
            num_flag[i]=0;
           }


        // 1000种情况，10个数可重复的情况
//            box[box_id]=i;
//            put_to_box(box_id+1);
       }


}

int main()
{

    put_to_box(0);
    printf("total=%d\n",total);
   return 1;
}
