from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image, Spacer, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from tkinter import messagebox

def generar_reporte_pdf(data_list, encabezado, nombre_archivo, titulo_reporte):
    lista = data_list
    if lista:
        try:
            # Crear un nuevo documento PDF con tamaño de hoja carta y márgenes adecuados
            pdf_filename = f"reports/{nombre_archivo}.pdf"
            doc = SimpleDocTemplate(pdf_filename, pagesize=letter,
                                    leftMargin=50, rightMargin=50, topMargin=100, bottomMargin=70)

            # Definir el logo de la empresa
            logo_path = "images/logo_reportes.jpg"
            logo = Image(logo_path, width=100, height=80)

            # Definir el contenido del pie de página
            contact_info = Paragraph("<br/>Teléfono: 730-xxx-78 <br/>Correo electrónico: miguel.040.net@gmail.com",
                                    style=getSampleStyleSheet()["Normal"])
            
            # Crear el título del reporte
            styles = getSampleStyleSheet()
            titulo = Paragraph(titulo_reporte, styles['Title'])


            # Función para agregar encabezado y pie de página en cada página del PDF
            def encabezado_y_pie(canvas, doc):
                # Añadir el logo al encabezado
                canvas.saveState()
                logo.drawOn(canvas, doc.leftMargin, doc.height + doc.topMargin - logo.drawHeight)
                
                # Añadir el título al encabezado
                titulo.wrap(doc.width, doc.topMargin)
                titulo.drawOn(canvas, doc.leftMargin, doc.height + doc.topMargin - 60)

                # Línea separadora entre el encabezado y el cuerpo
                canvas.setStrokeColor(colors.black)
                canvas.setLineWidth(1)
                canvas.line(doc.leftMargin, doc.height + doc.topMargin - logo.drawHeight - 5, doc.width + doc.leftMargin, doc.height + doc.topMargin - logo.drawHeight - 5)
                
                # Añadir información de contacto al pie de página
                contact_info.wrap(doc.width, doc.bottomMargin)
                contact_info.drawOn(canvas, doc.leftMargin, doc.bottomMargin - 20)
                
                # Línea separadora entre el cuerpo y el pie de página
                canvas.line(doc.leftMargin, doc.bottomMargin + 15, doc.width + doc.leftMargin, doc.bottomMargin + 15)
                canvas.restoreState()

            # Configurar los datos de los empleados en una tabla
            data = encabezado
            for datos in lista:
                data.append(datos)

            # Crear la tabla y darle formato
            table = Table(data)
            table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                    ('GRID', (0, 0), (-1, -1), 1, colors.black)]))  # Agregar líneas de separación

            # Generar el PDF con encabezado, leyenda y pie de página en cada página
            doc.build([Spacer(0.2, inch), table], onFirstPage=encabezado_y_pie, onLaterPages=encabezado_y_pie)

            messagebox.showinfo("Éxito", f"Reporte generado correctamente: {pdf_filename}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo generar el reporte: {e}")
    else:
        messagebox.showwarning("Advertencia", "No hay datos para generar el reporte.")
