# def confirm_ace(self):
    #     while (True):
    #         pg.display.set_caption('Confirmation') # Name the window
    #         pg.display.set_icon(pg.image.load('Images/Chips/blue_chip.png').convert()) # Set Icon
    #         self.mousePos = pg.mouse.get_pos()
    #         self.screen.fill('forestgreen')
    #         self.newCard.draw(self.screen,self.screen.get_width() * 0.5,self.screen.get_height() * 0.75)
    #         self.confirmText = self.chipFont.render('Choose the value...', True, 'White','forestgreen')
    #         self.confirmTextRect = self.confirmText.get_rect(center = (self.screen.get_width() * 0.5, self.screen.get_height() * 0.25))
    #         self.screen.blit(self.confirmText,self.confirmTextRect)
    #         if (self.hand + 11 <= 21):
    #             self.elevenButton = Button.Button(image=pg.image.load('Images/default_button_1.png'),pos=((self.screen.get_width() * 0.35),(self.screen.get_height() * 0.75)),text_input='11',font=self.uiFont,base_color='white',hovering_color='yellow')
    #             self.elevenButton.changeColor(self.mousePos)
    #             self.elevenButton.resize(160,160)
    #             self.elevenButton.update(self.screen)
    #         if (self.hand + 1 < 21):
    #             self.oneButton = Button.Button(image=pg.image.load('Images/default_button_1.png'),pos=((self.screen.get_width() * 0.65),(self.screen.get_height() * 0.75)),text_input='1',font=self.uiFont,base_color='white',hovering_color='yellow')
    #             self.oneButton.changeColor(self.mousePos)
    #             self.oneButton.resize(160,160)
    #             self.oneButton.update(self.screen)
    #         else:
    #             self.currCardVal = 1
    #             self.screen.fill('forestgreen')
    #             return
    #         for event in pg.event.get():
    #             if event.type == pg.QUIT:
    #                 pg.quit()
    #                 exit()
    #             if event.type == pg.MOUSEBUTTONDOWN:
    #                 if self.elevenButton.checkForInput(self.mousePos) and self.hand + 11 <= 21:
    #                     self.currCardVal = 11
    #                     self.screen.fill('forestgreen')
    #                     return
    #                 if self.oneButton.checkForInput(self.mousePos) and self.hand + 1 < 21:
    #                     self.currCardVal = 1
    #                     self.screen.fill('forestgreen')
    #                     return
    #         pg.display.update()
    #         pg.display.flip()
    #         self.frameSpeed.tick(60)