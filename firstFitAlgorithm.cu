#include <stdio.h>

__global__ void binPacking (float *bins, float *items, float cap, int length)
{
  int x = 0;
  for(int i = 0; i < length; i++)
    {
      x = 0;
      if(items[i] > cap)
        {
          printf ("Element %f je veci od kapaciteta spremnika koji je %f. PREKID!\n", items[i], cap);
          break;
        }

      if(bins[0 * length + x] >= items[i])
        {
          bins[0 * length + x] -= items[i];
          bins[1 * length + x] += items[i];
        }
      else
        {
          while(bins[0 * length + x] < items[i])
            {
              x+=1;
            }
          bins[0 * length + x] -= items[i];
          bins[1 * length + x] += items[i];
          }
    }
}
