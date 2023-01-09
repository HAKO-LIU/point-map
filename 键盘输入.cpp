#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<windows.h>

//reset
const char h0 = 0x00; //0(10) h0 reset用
//header
const char h1 = 0xFF; //255(10) h1-h5 header用
const char h2 = 0x92; //146(10)
const char h3 = 0x00; //0(10)
const char h4 = 0xC0; //192(10)
const char h5 = 0x00; //0(10)


HANDLE hComm; //串口HANDLE
DWORD writesize; //写入端口的字节数


//选择用于通信的USB端口
int _SelectPort(char portname[])
{
	int num = 1;
	int cnt = 0;
	int i;
	int j;
	char portname1[100];
	char portname2[10][100];
	char port_num[10];

	while (num > 0 && num < 10){
		sprintf(port_num, "%d", num);
		strcpy(portname1, "COM");
		strcat(portname1, port_num);

		hComm = CreateFile(
			portname1,
			0,
			0,
			NULL,
			OPEN_EXISTING,
			FILE_ATTRIBUTE_NORMAL,
			NULL
			);

		if (hComm == INVALID_HANDLE_VALUE){
			CloseHandle(hComm);
		}
		else{
			printf("%s 可以连接\n", portname1);
			CloseHandle(hComm);
			strcpy(portname2[cnt], portname1);
			cnt++;
		}
		num++;
	}

	if (cnt == 0){
		printf("找不到可以连接端口");
		getchar();
		exit(1);
	}
	else if (cnt == 1){
		strcpy(portname, portname2[0]);
		printf("\n%s已连接", portname);
	}
	else{
		printf("\n找到多个端口 请选择\n");

		for (i = 0; i < cnt; i++){
			printf("%d.%s ", i + 1, portname2[i]);
		}
		do{
			printf("\n号选择:");
			scanf("%d", &i);
		} while (i < 1 || i > cnt);

		strcpy(portname, portname2[i - 1]);
		printf("\n%s已连接\n", portname);
	}
	return 0;
}

int _OpenHandle(char portname[])
{

        //通信条件设定
	hComm = CreateFile(
		portname,
		GENERIC_WRITE,
		0,
		NULL,
		CREATE_ALWAYS,
		FILE_ATTRIBUTE_NORMAL,
		NULL
		);

	DCB dcb;
	GetCommState(hComm, &dcb);
	dcb.BaudRate = 38400;
	dcb.ByteSize = 8;
	dcb.Parity = NOPARITY;
	dcb.StopBits = ONESTOPBIT;
	SetCommState(hComm, &dcb);
	return 0;

}

void _init()
{
	//header写入
	WriteFile(hComm, &h1, 1, &writesize, NULL);
	WriteFile(hComm, &h1, 1, &writesize, NULL);
	WriteFile(hComm, &h2, 1, &writesize, NULL);
	WriteFile(hComm, &h3, 1, &writesize, NULL);
	WriteFile(hComm, &h4, 1, &writesize, NULL);
	WriteFile(hComm, &h5, 1, &writesize, NULL);
}

int main(void)
{

	int x = 0; //行数
	int y = 0; //列数
	int qy;	//y的商	
	int my;	//y的余
	int i = 0; //列数（1字节转换后）
	int j = 0; //行数（1字节转换后）
	int val; //暂时放置读取的数值
	int cnt = 0; //读取数值的数组号
	int csvData[1536] = {}; //读取的数值
	int pin[32][48] = {}; //pin数值
	int pin_1byte[4][48] = {}; //将pin的数值转换为字节
	char portname[100];//用于通信的端口
	char output_char[256];//输出的字符
	char filename[256];//文件名称
	char filepath[256] = "Data storage file/";//文件相对路径
	FILE *fp = NULL;



	_SelectPort(portname);

	_OpenHandle(portname);


	while (1){


		do{
			printf("请输入想显示的字(输入0退出):");
			scanf("%s", &output_char);
			getchar();


			if (strcmp(output_char, "0") == 0 || strcmp(output_char, "?O") == 0) {

				//全pin 0送信
				_init();
				for (i = 0; i < 4; i++) {
					for (j = 0; j < 48; j++) {
						WriteFile(hComm, &h0, 1, &writesize, NULL);
					}
				}
				printf("结束");
				getchar();
				CloseHandle(hComm);
				return 0;
			}


			else{
				//根据字符名创建文件
				strcat(output_char, ".csv");
				strcpy(filename, filepath);
				strcat(filename, output_char);

				fopen_s(&fp, filename, "r");

				//错误处理
				if (fp == NULL) {
					printf("未找到文件，请重新输入\n");
				}
			}
		} while (fp == NULL);

		//CSV文件 读取
		while (fscanf(fp, "%d,", &val) != EOF){
			//0以外改为1
			if (val != 0){
				val = 1;
			}
			csvData[cnt] = val;
			cnt++;
		}

		cnt = 0;
		fclose(fp);

		//将值分配给pin
		for (y = 0; y < 32; y++){
			for (x = 0; x < 48; x++){
				pin[y][x] = csvData[cnt];
				cnt++;


				//显示模型
				if (pin[y][x] == 0){
					printf("  ");
				}
				else{
					printf("●");
				}
			}
			printf("\n");
		}

		cnt = 0;

		_init();

		//数值分成单字节
		for (y = 0; y < 32; y++) {
			for (x = 0; x < 48; x++) {
				qy = y / 8;
				my = y % 8;
				pin_1byte[qy][x] += pin[y][x] * pow(2.0, my);
			}
		}

		//数据传输
		for (i = 0; i < 4; i++) {
			for (j = 0; j < 48; j++) {
				WriteFile(hComm, &pin_1byte[i][j], 1, &writesize, NULL);
				pin_1byte[i][j] = 0;
			}
		}
	}

}
