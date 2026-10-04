/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */

package com.mycompany.resolucaotela;

import java.awt.Dimension;
import java.awt.Toolkit;

/**
 *
 * @author gusta
 */
public class ResolucaoTela {

    public static void main(String[] args) {
        Toolkit ferramentas = Toolkit.getDefaultToolkit();
        Dimension screensize = ferramentas.getScreenSize();
        int largura = screensize.width;
        int altura = screensize.height;
        System.out.println("O tamanho da sua tela é:");
        System.out.println(largura+"x"+altura);
    }
}
