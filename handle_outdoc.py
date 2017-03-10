# -*- coding: utf-8 -*-
import sys
if __name__ == '__main__':
    file_name = sys.argv[1]
    try: 
	f = open(file_name, 'r')		
    except IOError:
        print "Error: open  %s file error!" % file_name		
    else:    
	lines = f.readlines()        
    finally:
        if f:
            f.close()	
    newfile_name = None	
    index = 0
    list_len = len(lines)
    move_fa_index = 4
    for line in lines:		
        if line.find("局干上")>0:
            if newfile_name != None:
                try: 
                    new_f = open(newfile_name, 'w')		
                except IOError:
                    print "Error: open  %s file error!" % newfile_name		
                else:    
                    new_f.write(file_line)       
                finally:
                    if new_f:
                        new_f.close()	
            file_line = ''
            tmpstr = line.strip()            
            #print tmpstr[0:tmpstr.index('第')]+tmpstr[tmpstr.index('干'):]
            newfile_name = "./output/"+tmpstr[0:tmpstr.index('第')]+tmpstr[tmpstr.index('干'):]+'.ini'
        if line.find(' 昼夜')>0:
            move_fa_index = 0
        move_fa_index = move_fa_index +1
        if move_fa_index == 3:        
            #print line
            tmplinel = line.replace('　', '').split()
            tmpline = "　"+" 　　"+tmplinel[0]+"  "+tmplinel[1]+'  '+tmplinel[2]+'  '+tmplinel[3] \
            +'　 　　'+tmplinel[4]+' '+tmplinel[5]+' '+tmplinel[6]+' '+tmplinel[7]+'　'+tmplinel[8]+' '+tmplinel[9]+' '+tmplinel[10]
            #print tmpline
            file_line = file_line+tmpline+"\r\n"
        else:    
            file_line = file_line+line	
        #print file_line
        index=index+1

        if index == list_len and newfile_name != None:
            try: 
                new_f = open(newfile_name, 'w')		
            except IOError:
                print "Error: open  %s file error!" % newfile_name		
            else:    
                new_f.write(file_line)       
            finally:
                if new_f:
                    new_f.close()	

                    
