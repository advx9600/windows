 public static void Main()
    {
        // 填满map内的元素
        string[,] map = new string[4, 3];
        for(int i = 0; i < 12; i++)
        {
            GenerateRandom(map);
        }

        // 那么 Map是否已经填满呢？？

    }
    public static void GenerateRandom(string[,] map)
    {
        List<int> listX = new List<int>();
        List<int> listY = new List<int>();

		// 查找空元素
        for (int x = 0; x < map.GetLength(0); x++)
        {
            for (int y = 0; y < map.GetLength(1); y++)
            {
                if (map[x, y] == null)
                {
                    listX.Add(x);
                    listY.Add(y);
                }
            }
        }

        if (listX.Count > 0)
        {
            var x = listX[Random.Range(0, listX.Count - 1)];
            var y = listY[Random.Range(0, listY.Count - 1)];

            map[x, y] = x + " ," + y;
        }
    }
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

	
	
	
// 这样map其实无法填满，修改为
// var random = Random.Range(0, listX.Count - 1)
// var x = listX[random];           
// var y = listY[random];
