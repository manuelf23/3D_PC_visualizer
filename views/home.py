from tkinter import Tk, Button, Label, StringVar, Frame, Entry
from tkinter import filedialog as FileDialog

import numpy as np
import open3d as o3d
class Home(Frame):
    """ Vista principal de la aplicación."""

    def __init__(self, controller, parent):

        Frame.__init__(self, parent)
        
        self.rutaSV = StringVar()
        self.error = StringVar()

        framePath = Frame(self)
        selectButton = Button(framePath, text="Seleccionar", command=self.openFile)
        rutaLabel = Entry(framePath, textvariable=self.rutaSV, borderwidth=1, relief="solid", state='disabled')

        selectButton.pack(side='left', padx=10, pady=10)
        rutaLabel.pack(side='left', padx=10, pady=10, fill='x', expand=True)
        framePath.pack(fill='x')

        frameButton = Frame(self)
        errorLabel = Label(frameButton, textvariable=self.error, fg='red')
        selectButton = Button(frameButton, text="Visualizar", command=self.visualizar)
        selectButton.pack(pady=10)
        errorLabel.pack(pady=10)
        frameButton.pack()

    def openFile(self):
        """ Abre un menú contextual para seleccionar un path a ciertos archivos en específicos."""
        filetypes = [
            ('Archivos pcd', '*.pcd'), 
            ('Archivos ply','*.ply'), 
            ('Archivos xyz', '*.xyz'),
            ('Archivos xyzrgb', '*.pxyzrgbly'),
            ('Archivos xyzn', '*.xyzn'),
            ('Archivos pts', '*.pts')
            ]
        self.fichero = FileDialog.askopenfilename(title="Abrir un fichero", filetypes=filetypes)
        self.rutaSV.set(self.fichero)
        self.error.set('')

    def visualizar(self):
        """ Abre el visualizador de nube de puntos."""
        if self.rutaSV.get():
            pcd = o3d.io.read_point_cloud(self.rutaSV.get())
            downpcd = pcd.voxel_down_sample(voxel_size=0.05)
            o3d.visualization.draw_geometries([downpcd])
        else:
            self.error.set('Primero debe seleccionar un archivo')

      
       

