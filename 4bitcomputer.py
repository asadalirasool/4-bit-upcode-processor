from tkinter import *
import time


root=Tk()
newfont1=("Arial",13)
newfont=("Arial",15,"bold")
memoryworldfont=("Arial",12)
memoryworldfont1=("Arial",12,"bold")
root.geometry("1600x800")

area=Text(root,width=65,height=20,font=newfont1,border=6,pady=35)
inclabel=Label(root,text="Instructions",font=newfont)
inclabel.grid(row=0)
area.grid(row=1,column=0)


aclabel=Label(root,text="AC",font=newfont)                              #accumalator label
aclabel.place(x=160,y=500)
aclabelfram=LabelFrame(root,width=20)
aclabelfram.place(x=210,y=503)
acvalue="0000000000"
label1=Label(aclabelfram,text=acvalue,font=newfont1)
label1.pack()



                                                                      
                                                                       #program counter label
pclabel=Label(root,text="PC",font=newfont)
pclabel.place(x=160,y=540)
pcinput="0000000000000000"
pcframe=LabelFrame(root,width=20)
pcframe.place(x=210,y=543)
pcinputlabel=Label(pcframe,text=pcinput,font=newfont1)
pcinputlabel.pack()




                                                                        #Address register labels


arlabel=Label(root,text="AR",font=newfont)
arlabel.place(x=160,y=580)
arinput="0000000000000000"
arframe=LabelFrame(root,width=20)
arframe.place(x=210,y=583)
arinputlabel=Label(arframe,text=pcinput,font=newfont1)
arinputlabel.pack()








                                                                        #Data register label


drlabel=Label(root,text="DR",font=newfont)
drlabel.place(x=160,y=620)
drinput="0000000000"
drframe=LabelFrame(root,width=20)
drframe.place(x=210,y=623)
drinputlabel=Label(drframe,text=drinput,font=newfont1)
drinputlabel.pack()


                                                                        #instruction register label

irlabel=Label(root,text="IR",font=newfont)
irlabel.place(x=160,y=660)
irinput="0000000000000000"
irframe=LabelFrame(root,width=20)
irframe.place(x=210,y=663)
irinputlabel=Label(irframe,text=irinput,font=newfont1)
irinputlabel.pack()


    

                                                                        #Temporary register label


trlabel=Label(root,text="TR",font=newfont)
trlabel.place(x=160,y=700)
trinput="0000000000000000"
trframe=LabelFrame(root,width=20)
trframe.place(x=210,y=703)
trinputlabel=Label(trframe,text=trinput,font=newfont1)
trinputlabel.pack()




mprlabel=Label(root,text="MPR",font=newfont)
mprlabel.place(x=158,y=740)
mprinput="00000000000000000000000000000000"
mprframe=LabelFrame(root,width=20)
mprframe.place(x=210,y=743)
mprinputlabel=Label(mprframe,text=mprinput,font=newfont1)
mprinputlabel.pack()






                                                                             #RAM frame


ramframe=LabelFrame(root)
ramframe.place(x=900,y=70)
x=str(1)
raminput1="0000000000000000"
raminput2="0000000000000000"
raminput3="0000000000000000"
raminput4="0000000000000000"
raminput5="0000000000000000"
raminput6="0000000000000000"
raminput7="0000000000000000"
raminput8="0000000000000000"
raminput9="0000000000000000"
raminput10="0000000000000000"
raminput11="0000000000000000"
raminput12="0000000000000000"
raminput13="0000000000000000"
raminput14="0000000000000000"
raminput15="0000000000000000"
raminput16="0000000000000000"
raminput17="0000000000000000"
raminput18="0000000000000000"
raminput19="0000000000000000"
raminput20="0000000000000000"
raminput21="0000000000000000"
raminput22="0000000000000000"
raminput23="0000000000000000"
raminput24="0000000000000000"
raminput25="0000000000000000"
raminput26="0000000000000000"
raminput27="0000000000000000"
raminput28="0000000000000000"
raminput29="0000000000000000"
raminput30="0000000000000000"
raminput31="0000000000000000"
raminput32="0000000000000000"








ramlabellist=[]
raminputlist=[raminput1,raminput2,raminput3,raminput4,raminput5,raminput6,raminput7,raminput8,raminput9,raminput10,raminput11,raminput12,raminput13,raminput14,raminput15,raminput16,raminput17,raminput18,raminput19,raminput20,raminput21,raminput22,raminput23,raminput24,raminput25,raminput26,raminput27,raminput28,raminput29,raminput30,raminput31,raminput32]





x=0                                                         #variable for printing ramworlds

ramprint=Label(root,text="RAM",font=newfont)
ramprint.place(x=1170,y=25)





for labels in range(16):
   
   
   
   ramlabel=Label(ramframe,text=raminputlist[x],font=memoryworldfont)
   label=Label(ramframe,text=x,font=memoryworldfont1)
   label.grid(row=labels,column=0,padx=(25,10))
   x=x+1
   ramlabel.grid(row=labels,column=1)
   ramlabellist.append(ramlabel)

for labels in range(16):
    ramlabel111=Label(ramframe,text=raminputlist[x],font=memoryworldfont)
    label=Label(ramframe,text=x,font=memoryworldfont1)
    label.grid(row=labels,column=2,padx=(20,10))
    x=x+1
    ramlabel111.grid(row=labels,column=3,padx=(0,25))
    ramlabellist.append(ramlabel111)

      
   
instructions=[]
operand=[]
variableoperand=[]
fullinstruction=[]
binaryinstruction=[]
accumulator_entry=[]

def multbinart(nuuuu):
    mullll=int(nuuuu)
    mulbinary=format(mullll,'032b')
    return str(mulbinary)



def opbinary(operandbinary):
    aaa=int(operandbinary)
    opbinary=format(aaa,'016b')
    return str(opbinary)




def binarycon(number):
    aa=int(number)
    binary=format(aa,'010b')
    return binary


def full_inc_fun(inc):
    for ind in fullinstruction:
        t=ind.find(" ")
        tt=ind[t:]
        print("aaaaaaaaa")
        print(tt)

        ttt=ind[0:t-1]
        print(ttt)
        
        if(ttt==inc):
            return tt
        

    



pcvar=0
mprlist=[]


def instrc_load_in_memory():                                                    #instruction load manuplation
    memory_load_counter=0
    binvar=0
    operand_after_this=len(instructions)
    if(instructions[-1]!="HALT"):                                            
        print("Hault instuctions is not Written")
    for instruction in instructions:
        if(instruction=="ADD"):
            cccccc=operand[binvar]
            
            xc=full_inc_fun(cccccc)
            binvar+=1
            no=binarycon(xc)
            operandd=str(no)
            text1="000010"+operandd
            binaryinstruction.append(text1)
            
                
            ramlabellist[memory_load_counter].config(text=text1)
                
                
            memory_load_counter+=1
                
                
                
                
        elif(instruction=="SUB"):
            cccccc=operand[binvar]
            
            xc=full_inc_fun(cccccc)
            binvar+=1
            no=binarycon(xc)
            suboperandd=str(no)
            
            subtext="000100"+suboperandd 
            binaryinstruction.append(subtext)
            ramlabellist[memory_load_counter].config(text=subtext)
            memory_load_counter+=1
        elif(instruction=="MULT"):
            cccccc=operand[binvar]
            
            xc=full_inc_fun(cccccc)
            binvar+=1
            no=binarycon(xc)
            muloperand=str(no)





            mulno=binarycon(xc)
            muloperand=str(mulno)
            multext="000110"+muloperand
            binaryinstruction.append(multext)
            ramlabellist[memory_load_counter].config(text=multext)
            memory_load_counter+=1
        elif(instruction=="AND"):
            cccccc=operand[binvar]
            
            xc=full_inc_fun(cccccc)
            binvar+=1
            no=binarycon(xc)
            andoperand=str(no)
            andno=binarycon(xc)
            andoperand=str(andno)
            andtext="000011"+andoperand
            binaryinstruction.append(andtext)
            ramlabellist[memory_load_counter].config(text=andtext)
            memory_load_counter+=1
        elif(instruction=="OR"):
            cccccc=operand[binvar]
            
            xc=full_inc_fun(cccccc)
            binvar+=1
            no=binarycon(xc)
            oroperand=str(no)
            orno=binarycon(xc)
            oroperand=str(orno)
            ortext="000111"+oroperand
            binaryinstruction.append(ortext)
            ramlabellist[memory_load_counter].config(text=ortext)
            memory_load_counter+=1
        elif(instruction=="STD"):
            cccccc=operand[binvar]
            
            xc=full_inc_fun(cccccc)
            binvar+=1
            no=binarycon(xc)
            stdoperand=str(no)
            stdno=binarycon(xc)
            stdoperand=str(stdno)
            stdtext="000001"+stdoperand
            binaryinstruction.append(stdtext)
            ramlabellist[memory_load_counter].config(text=stdtext)
            memory_load_counter+=1
        elif(instruction=="NOR"):
            cccccc=operand[binvar]
            
            xc=full_inc_fun(cccccc)
            binvar+=1
            no=binarycon(xc)
            noroperand=str(no)
            norno=binarycon(xc)
            noroperand=str(norno)
            notext="001000"+noroperand
            binaryinstruction.append(notext)
            ramlabellist[memory_load_counter].config(text=notext)
            memory_load_counter+=1
        elif(instruction=="NAND"):
            cccccc=operand[binvar]
            
            xc=full_inc_fun(cccccc)
            binvar+=1
            no=binarycon(xc)
            nandoperand=str(no)
            nandno=binarycon(xc)
            nandoperand=str(nandno)
            nandtext="001001"+nandoperand
            binaryinstruction.append(nandtext)
            ramlabellist[memory_load_counter].config(text=nandtext)
            memory_load_counter+=1
        elif(instruction=="LDA"):
            cccccc=operand[binvar]
            
            xc=full_inc_fun(cccccc)
            binvar+=1
            no=binarycon(xc)
            ldaoperand=str(no)
            ldano=binarycon(xc)
            ldaoperand=str(ldano)
            ldatext="000000"+ldaoperand
            binaryinstruction.append(ldatext)
            ramlabellist[memory_load_counter].config(text=ldatext)
            memory_load_counter+=1
        elif(instruction=="ISZ"):
            isztext="0001010000000000"
            binaryinstruction.append(isztext)
            ramlabellist[memory_load_counter].config(text=isztext)
            memory_load_counter+=1
        elif(instruction=="BUN"):
            buntext="0010100000000000"
            binaryinstruction.append(buntext)
            ramlabellist[memory_load_counter].config(text=buntext)
            memory_load_counter+=1
        elif(instruction=="BSA"):
            bsatext="0010110000000000"
            binaryinstruction.append(bsatext)
            ramlabellist[memory_load_counter].config(text=bsatext)
            memory_load_counter+=1
        elif(instruction=="SKP"):
            cccccc=operand[binvar]
            
            xc=full_inc_fun(cccccc)
            binvar+=1
            no=binarycon(xc)
            skpoperand=str(no)
            skpno=binarycon(xc)
            skpoperand=str(skpno)
            skptext="001100"+skpoperand
            binaryinstruction.append(skptext)
            ramlabellist[memory_load_counter].config(text=skptext)
            memory_load_counter+=1
        elif(instruction=="STM"):
            stmtext="0011010000000000"
            binaryinstruction.append(stmtext)
            ramlabellist[memory_load_counter].config(text=stmtext)
            memory_load_counter+=1
       # else:
        #    u=0
         #   varno=opbinary(variableoperand[u])
          #  varno1=str(varno)
           # u+=1
            #ramlabellist[memory_load_counter].config(text=varno1)
    pcinputlabel.config(text=opbinary(pcvar))        
            
stmmem=len(binaryinstruction)+1              

def runbtnfun():
    aaaaa=0
    global stmmem
    global pcvar
    for index, innnn in enumerate(binaryinstruction):
        if(innnn==None or innnn==0):
            break
        else:
            bajwa=innnn[2:6]
            bajwa1=innnn[6:]
            root.after(1000,arinputlabel.config(text=opbinary(pcvar)))
            
            if aaaaa<len(binaryinstruction):
                
                pcvar+=1
                root.after(1000,pcinputlabel.config(text=opbinary(pcvar)))
                
        
            irinputlabel.config(text=innnn)
            aaaaa+=1

            root.after(1000,drinputlabel.config(text=bajwa1))
            
            if(bajwa=="0000"):
                root.after(1000,label1.config(text=bajwa1))
                accumulator_entry.append(bajwa1)
            print(bajwa)    
            print(bajwa1)
                
            if(bajwa=="0010"):
                print("called")
                dec=int(accumulator_entry[-1],2)
                dec1=int(bajwa1,2)
                
                dec2=dec+dec1
                print(dec2)
                dec3=binarycon(dec2)
                print(dec3)
                label1.config(text=dec3)
                accumulator_entry.append(dec3)


            if(bajwa=="0011"):
                print("And called")
                anddec=int(accumulator_entry[-1],2)
                anddec1=int(bajwa1,2)
                anddec2=anddec&anddec1
                anddec3=binarycon(anddec2)
                label1.config(text=anddec3)
                accumulator_entry.append(anddec3)
            if(bajwa=="0100"):
                print("Sub called")
                subdec=int(accumulator_entry[-1],2)
                subdec1=int(bajwa1,2)
                subdec2=subdec-subdec1
                subdec3=binarycon(subdec2)
                label1.config(text=subdec3)
                accumulator_entry.append(subdec3)

            if(bajwa=="0110"):
                print("MULT called")
                multdec=int(accumulator_entry[-1],2)
                multdec1=int(bajwa1,2)
                multdec3=multdec*multdec1
                mult4=binarycon(multdec3)
                
                mprinputlabel.config(text=multbinart(multdec3))
                mprlist.append(mult4)


            if(bajwa=="0111"):
                print("or called")
                ordec=int(accumulator_entry[-1],2)
                ordec1=int(bajwa1,2)
                ordec3=ordec | ordec1
                label1.config(text=binarycon(ordec3))
                accumulator_entry.append(ordec3)    
            if(bajwa=="1000"):
                print("nor called")
                nordec=int(accumulator_entry[-1],2)
                nordec1=int(bajwa1,2)
                nodec2=~(nordec|nordec1)
                nordec3=binarycon(nodec2)
                label1.config(text=nordec3)
                accumulator_entry.append(nordec3)

            if(bajwa=="1001"):
                nanddec=int(accumulator_entry[-1],2)
                nanddec1=int(bajwa1,2)
                nanddec2=~(nanddec&nanddec1)
                nanddec3=binarycon(nanddec2)
                label1.config(text=nanddec3)
                accumulator_entry.append(nanddec3)
            if(bajwa=="0001"):
                stdval=accumulator_entry[-1]
                stddec1=int (bajwa1,2)
                ramlabellist[stddec1].config(text="000000"+stdval)

            if(bajwa=="1101"):
                stmval=mprlist[-1]
                stmvalhalf=stmval[0:15]
                stmsecondhalf=stmval[16:31]
                ramlabellist[stmmem].config(text=stmvalhalf)
                ramlabellist[stmmem+1].config(text=stmsecondhalf)





                



                     

            
            




def loadfun():                                                      #load btn clickfunction
    inputtext=area.get("1.0","end")
    lines=inputtext.split("\n")
    
    
    
    for line in lines:
        if(line==""):
            continue
        else:
            if(line=="HALT"):
                instructions.append(line)
            else:
                fullinstruction.append(line)
                collon_index=line.find(":") 
                if collon_index!=-1:
                    s=line[collon_index+1:]
                    ss=line[0:collon_index]
                    instructions.append(ss)
                    variableoperand.append(s)
                    

                       
                else:
                    spno=line.find(" ")
                    oper=line[spno+1:]

                    inst=line[0:spno]
                    instructions.append(inst)
                    operand.append(oper)
                    print(inst)
                    print (oper)    


    instrc_load_in_memory()
    



runbtn=Button(root,text="Run",font=memoryworldfont1,padx=6,pady=8,command=runbtnfun)
runbtn.place(x=700,y=150)
loadbtn=Button(root,text="Load",font=memoryworldfont1,padx=5,pady=5,command=loadfun)                                                                                #load button
loadbtn.place(x=700,y=200)






root.mainloop()