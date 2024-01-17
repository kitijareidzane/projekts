import fitz
import re
import os

def atrast_vardu(folder_path):
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        print(f"Mapes nav: {folder_path}")
        return
    
    specif_vards=input("Ievādiet vārdu, kuru vēlaties atrast CV: ")
    visi_vardi=False
    for f_nosaukums in os.listdir(folder_path):
        failu_path=os.path.join(folder_path, f_nosaukums)
        if failu_path.lower().endswith('.pdf'):
            print(f"Tiek meklēts'{specif_vards}' failā: {failu_path}")


            pdf_dokuments=fitz.open(failu_path)
            vards_ir=False

    for lpp_num in range(pdf_dokuments.page_count):
        lpp=pdf_dokuments[lpp_num]
        lpp_teksts=lpp.get_text()

        rindas=lpp_teksts.split('\n')
        for rindas_num, rinda in enumerate(rindas, start=1):
            if specif_vards.lower() in rinda.lower():
                print(f"Vārds '{specif_vards}' atrasts {lpp_num+1} .lpp, rindā: {rindas_num}, failā: {failu_path}")
                print(f"  {rinda.strip()}")
                vards_ir=True
                visi_vardi=True

    pdf_dokuments.close()
    if not vards_ir:
        print(f"Vārds '{specif_vards}' netika atrasts failā: {failu_path}.")

    if not visi_vardi:
        print(f"Vārds '{specif_vards}'netika atrasts")

folder_path='CV'
atrast_vardu(folder_path)        

