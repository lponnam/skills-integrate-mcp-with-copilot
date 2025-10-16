<div class="row">
	
	<div class="col-md-12 col-sm-12 clearfix" style="text-align:center;">
		<h2 style="font-weight:200; margin:0px; color: #FF9900"><?php echo $system_name;?></h2>
    </div>
	
	<!-- Raw Links -->
	<div class="col-md-12 col-sm-12 clearfix ">
		
        <ul class="list-inline links-list pull-left">
        <!-- Language Selector -->	
				
           <li class="dropdown language-selector">
		   <strong style="color:#FF0000">Running Session:&nbsp;<?php echo $running_session;?></strong>
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" data-close-others="true">
                        	<i class="entypo-user"></i><?php echo $this->session->userdata('login_type');?>
                    </a>
		
				<?php if ($account_type != 'parent'):?>
				<ul class="dropdown-menu <?php if ($text_align == 'right-to-left') echo 'pull-right'; else echo 'pull-left';?>">
					<li>
						<a href="<?php echo base_url();?>index.php?<?php echo $account_type;?>/manage_profile">
                        	<i class="entypo-info"></i>
							<span><?php echo get_phrase('edit_profile');?></span>
						</a>
					</li>
					<li>
						<a href="<?php echo base_url();?>index.php?<?php echo $account_type;?>/manage_profile">
                        	<i class="entypo-key"></i>
							<span><?php echo get_phrase('change_password');?></span>
						</a>
					</li>
				</ul>
				<?php endif;?>
				<?php if ($account_type == 'parent'):?>
				<ul class="dropdown-menu <?php if ($text_align == 'right-to-left') echo 'pull-right'; else echo 'pull-left';?>">
					<li>
						<a href="<?php echo base_url();?>index.php?parents/manage_profile">
                        	<i class="entypo-info"></i>
							<span><?php echo get_phrase('edit_profile');?></span>
						</a>
					</li>
					<li>
						<a href="<?php echo base_url();?>index.php?parents/manage_profile">
                        	<i class="entypo-key"></i>
							<span><?php echo get_phrase('change_password');?></span>
						</a>
					</li>
				</ul>
				<?php endif;?>
			</li>
        </ul>
        
        
		<ul class="list-inline links-list pull-right">
			           <li class="dropdown language-selector">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" data-close-others="true">
                         <span class="label label-success"><i class="entypo-globe"></i>&nbsp;Change Language&nbsp;<i class="entypo-down"></i></span>
                    </a>
				
				<ul class="dropdown-menu <?php if ($text_align == 'left-to-right') echo 'pull-left'; else echo 'pull-right';?>">
					<?php
                            $fields = $this->db->list_fields('language');
                            foreach ($fields as $field)
                            {
                                if($field == 'phrase_id' || $field == 'phrase')continue;
                                ?>
                                    <li class="<?php if($this->session->userdata('current_language') == $field)echo 'active';?>">
                                        <a href="<?php echo base_url();?>index.php?multilanguage/select_language/<?php echo $field;?>">
                                            <img src="assets/images/flag/<?php echo $field;?>.png" style="width:16px; height:16px;" />	
												 <span><?php echo $field;?></span>
                                        </a>
                                    </li>
                                <?php
                            }
                            ?>
                    
				</ul>
				
			</li>
			
			<li class="sep"></li>
			
			<li>
				<a href="<?php echo base_url();?>index.php?login/logout">
					Log Out <i class="entypo-logout right"></i>
				</a>
			</li>
		</ul>				
	</div>
	<br>
		<h3 align="center" style="color:#FF0000">You are Using Demo Version of Optimum School System. You can Purchase the Full Source Code with just $100: 	<form method="POST" action="https://voguepay.com/pay/" target="_blank"><input type="hidden" name="v_merchant_id" value="1567-0045444" /><input type="hidden" name="memo" value="Order from OPTIMUM LINKUP COMPUTER" /><input type="hidden" name="cur" value="NGN" /><input type="hidden" name="item_1" value="Software" /><input type="hidden" name="price_1" value="39800" /><input type="hidden" name="description_1" value="You are about to purchase single license Optimum School System. Note that download link will be sent to your email immediately your payment is sucessfull. Therefore, kinly supply your correct email address during the payment process. click on the payment card below to continue" /><br /><input type="image" src="https://voguepay.com/images/buttons/buynow_red.png" alt="PAY" /></form>  Online Demo Link : <a href="https://optimumlinkupsoftware.com/school" target="_blank"><span class="label label-info">Here</span></h3>
</div>



<hr style="margin-top:0px;" />

